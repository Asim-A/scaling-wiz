import os
from typing import Dict
from dotenv import load_dotenv
from InquirerPy import prompt
from InquirerPy.base.control import Choice
import pyperclip
from enum import Enum


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
    LABEL = 11


class Database(Enum):
    MONGO = "mongodb"
    POSTGRES = "postgres"


class Phase(Enum):
    LOAD = "load"
    RUN = "run"
    LOAD_RUN = "both"


class Workload(Enum):
    UPDATE_HEAVY = "WorkloadA-UH"
    READ_MOSTLY = "WorkloadB-RM"
    READ_ONLY = "WorkloadC-RO"

class QuestionParser():
    def pad_str(self, s: str) -> str:
        return f" {s} "

    def logs_path(self) -> str:
        return "~/logs"

    def benchmark_path(self) -> str:
        return "~/benchmark/ycsb-0.17.0"

    def workload_path(self, workload: str) -> str:
        return f"{self.benchmark_path()}/workloads/{workload}"

    def monogo_url(self): 
        return f"-p mongodb.url=\"mongodb://{self.username}:{self.password}@{self.ip}:{self.port}/{self.dbname}?authSource=admin&authMechanism=SCRAM-SHA-256\""
    
    def postgres_prefix(self, key: str, value: str):
        prefix = "postgrenosql"
        return f"-p {prefix}.{key}={value}"

    def postgres_url(self):
        return f"""-p jdbc:postgresql://localhost:5432/{self.db} {self.postgres_prefix("username", self.db)} {self.postgres_prefix("passwd", self.password)} {self.postgres_prefix("autocommit", "true")}"""
    

    def setup(self, results: Dict):
        print(Question.DATABASE)
        val = Question.DATABASE
        print(val)

        self.db = results[Question.DATABASE.value]
        self.ip = results[Question.IP.value]
        self.port = results[Question.PORT.value]
        self.dbname = results[Question.DBNAME.value]
        self.username = results[Question.USERNAME.value]
        self.password = results[Question.PASSWORD.value]
        self.thread_count = results[Question.THREADS.value]
        self.workload = results[Question.WORKLOAD.value]
        self.phase = results[Question.PHASE.value]
        self.record_count = results[Question.RECORDCOUNT.value]
        self.operation_count = results[Question.OPERATIONCOUNT.value]
        self.label = results[Question.LABEL.value]

    def phase_cmd(self) -> str: 
        s = ""
        if self.phase == Phase.LOAD:
            s += Phase.LOAD.value
        elif self.phase == Phase.RUN or self.phase == Phase.LOAD_RUN:
            s += Phase.RUN.value
        else:
            s = ""
        
        return self.pad_str(s)

    
    def database_cmd(self) -> str:
        s = ""
        if self.db == Database.MONGO:
            s += f"mongodb {self.monogo_url()}"
        elif self.db == Database.POSTGRES:
            s += f"postgrenosql {self.postgres_url()}"
        else: 
            s = ""
        
        return self.pad_str(s)

    def workload_cmd(self) -> str:
        s = "-P "
        if self.workload == Workload.UPDATE_HEAVY:
             s += self.workload_path("workloada")
        elif self.workload == Workload.READ_MOSTLY:
            s += self.workload_path("workloadb")
        elif self.workload == Workload.READ_ONLY:
            s += self.workload_path("workloadc")
        else:
            s = ""
        
        return self.pad_str(s)
        
    
    def thread_count_cmd(self):
        return self.pad_str(f"-p threadcount={self.thread_count}")
    
    def operation_count_cmd(self):
        return self.pad_str(f"-p operationcount={self.operation_count}")
    
    def record_count_cmd(self):
        return self.pad_str(f"-p recordcount={self.record_count}")

    # date +'%Y-%m-%d_%H:%M'
    def log_cmd(self):
        s = f" > {self.logs_path()}/$(date +'%Y-%m-%d_%H+%M')_{self.db.value}_{self.phase.value}_{self.workload.value}_r{self.amount_convert(self.record_count)}_op{self.amount_convert(self.operation_count)}"
        if self.label:
            s += f"_{self.label}"
        s += ".log"
        return s

    def amount_convert(self, amount_str: str) -> str:
        amount = int(amount_str)

        if amount >= 1_000_000_000:
            return f"{int(amount/1_000_000_000)}B"
        elif amount >= 1_000_000:
            return f"{int(amount/1_000_000)}M"
        elif amount >= 1_000:
            return f"{int(amount/1_000)}K"

        return amount_str

    def __init__(self, results: Dict):
        if len(results) != len(Question):
            raise Exception("Not enough questions answered.")
        
        self.setup(results)

        # ./bin/ycsb run mongodb -s -P workloads/workloada -p mongodb.url="mongodb://ycsb:NTNU1elns@localhost:27017/ycsb?authSource=admin&authMechanism=SCRAM-SHA-256" -p threadcount=4 -p operationcount=10000000
        self.command = ""

        self.command += f"{self.benchmark_path()}/bin/ycsb"
        self.command += self.phase_cmd()
        self.command += self.database_cmd()
        self.command += self.workload_cmd()
        self.command += self.thread_count_cmd()
        self.command += self.record_count_cmd()
        self.command += self.operation_count_cmd()
        self.command += self.log_cmd()

    def get_command(self) -> str:
        return self.command.strip()

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
            "default": "10.24.166.125"
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
        },
        {
            "type": "input",
            "message": "Label:"
        }
    ]

    return questions


def main():
    questions = question_setup()
    results = prompt(questions=questions)

    try:
        parsed = QuestionParser(results)
        print("Command:")
        print(parsed.get_command())
        pyperclip.copy(parsed.get_command())
    except Exception:
        exit()


if __name__ == "__main__":
    main()
