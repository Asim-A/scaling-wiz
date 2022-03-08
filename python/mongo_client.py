import os
import time
from typing import Tuple, Collection, Dict, List
from dotenv import load_dotenv
import pymongo
import requests


class ConnectionString:

    def __init__(self) -> None:
        self.connection_string = self._get_connection_string()

    def _get_connection_string(self) -> str:
        load_dotenv()
        username = os.getenv("username")
        password = os.getenv("password")
        addr = os.getenv("addr")
        cloud = "+srv" if os.getenv("isCloud") else ""
        cloudNet = ".mongodb.net" if os.getenv("isCloud") else ""

        conn_str = f"mongodb{cloud}://{username}:{password}@{addr}{cloudNet}/?retryWrites=true&w=majority"

        return conn_str

    def get(self) -> str:
        print(self.connection_string)
        return self.connection_string


class RandomApi:

    def __init__(self) -> None:
        self.api_url = "https://randomuser.me/api"
        print(self.api_url)

    def get_random_users(self, amount: int = 1000) -> Tuple[bool, Dict]:
        if amount < 1 or amount > 5000:
            print("It is only possible to retreive 1-5000 random users.")

        url = f"{self.api_url}/?results={str(amount)}"
        print(f"url: {url}, doing request")
        r = requests.get(url, timeout=5)

        if r.status_code == 200:
            print("success")
            return (True, r.json())
        else:
            print(r.status_code)
            print(r.reason)
            return (False, {})


class MongoHub:
    def __init__(self, database: str) -> None:
        self.cs = ConnectionString()
        self.client = pymongo.MongoClient(
            self.cs.get(), serverSelectionTimeoutMS=5000)

        (is_connected, db_names) = self.is_connection_established()
        if (is_connected):
            print(f"Successfully connected, available databases: {db_names}")

        if database:
            self.db = self.client[database]

    def is_connection_established(self) -> Tuple[bool, List[str]]:

        try:
            names = self.client.list_database_names()
            return (True, names)

        except Exception:
            print("Unable to connect to the server.")
            return (False, list())

    def is_using_db(self) -> bool:
        if self.db is not None:
            return True

        return False

    def set_db(self, database: str) -> bool:
        (is_connected, dbs) = self.is_connection_established()

        if is_connected and database:
            self.db = self.client[database]
            return True

    def create_collection(self, collection_name: str, values, should_purge_old: bool = False) -> Collection:
        if not self.is_using_db():
            print("Please set DB first")
            return

        collection_list = self.db.list_collection_names()
        col = self.db[collection_name]

        if collection_name in collection_list and should_purge_old:
            col.delete_many({})

        start_time = time.time()
        col.insert_many(values)
        print(f"Took: {time.time() - start_time} seconds to insert {len(values)} elements.")

        return col


mh = MongoHub("py")
amountOfUsers = 5000
random_users_api = RandomApi()
success, res = random_users_api.get_random_users(amountOfUsers)

if success:
    users = res["results"]
    mh.create_collection("users", users, True)
