from peewee import Model, CharField, IntegerField, DateTimeField, ForeignKeyField, SqliteDatabase
from datetime import datetime


db = SqliteDatabase("./database/companyDetails.db")

class VantageModel(Model):
    class Meta:
        database = db

class Company(VantageModel):
    id = IntegerField(primary_key=True)
    name = CharField(unique=True,max_length=100)
    address = CharField(max_length=255)
    contact_person = CharField(max_length=100)
    contact_number = CharField(max_length=10)
    email = CharField(max_length=255)
    