import os
from typing import Collection, Dict
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
        conn_str = f"mongodb+srv://{username}:{password}@{addr}.mongodb.net/?retryWrites=true&w=majority"

        return conn_str

    def get(self) -> str:
        print(self.connection_string)
        return self.connection_string


class RandomApi:

    def __init__(self) -> None:
        self.api_url = "https://randomuser.me/api"
        pass

    def get_random_users(self, amount: int = 1000) -> tuple[bool, Dict]:
        if amount < 1 or amount > 5000:
            print("It is only possible to retreive 1-5000 random users.")

        url = f"{self.api_url}/?results={str(amount)}"
        print(f"url: {url}")
        r = requests.get(url)

        if r.status_code == 200:
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

        (is_connected, db_names) = self.is_connection_establised()
        if (is_connected):
            print(f"Successfully connected, available databases: {db_names}")

        if database:
            self.db = self.client[database]

    def is_connection_establised(self) -> tuple[bool, list[str]]:

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
        (is_connected, dbs) = self.is_connection_establised

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

        col.insert_many(values)

        return col


mh = MongoHub("py")
random_users_api = RandomApi()
success, res = random_users_api.get_random_users(100)


if success:
    users = res["results"]

    mh.create_collection("users", users, True)
