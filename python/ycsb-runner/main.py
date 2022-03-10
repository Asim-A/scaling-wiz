import os
from typing import Dict
from dotenv import load_dotenv
from InquirerPy import prompt
from InquirerPy.base.control import Choice
from enum import Enum, auto


class Question(Enum):
    DATABASE = 0
    IP = 1
    PORT = 2
    DBNAME = 3
    USERNAME = 4
    PASSWORD = 5
    THREADS = 6
    WORKLOAD = 7
    PHASE = 8
    RECORDCOUNT = 9
    OPERATIONCOUNT = 10


class Database(Enum):
    MONGO = auto()
    POSTGRES = auto()


class Phase(Enum):
    LOAD = auto()
    RUN = auto()
    LOAD_RUN = auto()


class Workload(Enum):
    UPDATE_HEAVY = auto()
    READ_MOSTLY = auto()
    READ_ONLY = auto()


class QuestionParser():

    def __init__(self, results: Dict) -> str:
        if len(results) != len(Question):
            raise Exception("Not enough questions answered.")

        items = list(results.values())

        s = ""
        for i in items:
            s += f"{i} "

        s = s.rstrip()
        print(s)
        print(f"last char: {ord(s[len(s)-1])}")
        print(f"last char: {ord(s[-1])}")

        return s


def question_setup():
    load_dotenv()
    password = os.getenv("password")
    questions = [
        {
            "type": "list",
            "message": "Which database?",
            "choices": [
                Choice(Database.MONGO, "MongoDB", enabled=True),
                Choice(Database.POSTGRES, "PostgreSQL")
            ]
        },
        {
            "type": "input",
            "message": "IP-Address:",
            "default": "localhost"
        },
        {
            "type": "input",
            "message": "Port:",
            "default": "27017"
        },
        {
            "type": "input",
            "message": "Database Name:",
            "default": "ycsb"
        },
        {
            "type": "input",
            "message": "Username:",
            "default": "ycsb"
        },
        {
            "type": "password",
            "message": "Password:",
            "default": password
        },
        {
            "type": "list",
            "message": "Threads to use:",
            "choices": [1, 2, 3, 4],
            "default": 4
        },
        {
            "type": "list",
            "message": "Workload:",
            "choices": [
                Choice(Workload.UPDATE_HEAVY, "Update Heavy (Workload A)"),
                Choice(Workload.READ_MOSTLY, "Read Mostly (Workload B)"),
                Choice(Workload.READ_ONLY, "Read Only (Workload C)")
            ]
        },
        {
            "type": "list",
            "message": "Phase:",
            "choices": [
                Choice(Phase.LOAD, "Load"),
                Choice(Phase.RUN, "Run"),
                Choice(Phase.LOAD_RUN, "Load then Run (Both)", enabled=True)
            ]
        },
        {
            "type": "input",
            "message": "Record Count:",
            "default": "100000"
        },
        {
            "type": "input",
            "message": "Operation Count:",
            "default": "100000"
        }
    ]

    return questions


def main():
    questions = question_setup()
    result = prompt(questions=questions)

    try:
        shell_string = QuestionParser(result)
        print(shell_string)
        print(f"last char: {shell_string[len(shell_string)-1]}")
    except Exception:
        exit()


if __name__ == "__main__":
    main()
