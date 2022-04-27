from datetime import datetime
from peewee import Model, SqliteDatabase, DateTimeField, CharField

db = SqliteDatabase("commands.db")


class BaseModel(Model):
    added_at = DateTimeField()

    def __init_(self):
        self.added_at = datetime.utcnow()

    class Meta:
        database = db


class Command(BaseModel):
    last_used = DateTimeField()

    pass
