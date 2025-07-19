from peewee import Model, CharField, DateTimeField
from data_base.data_base import db
import datetime
class Costumer(Model):
    Name = CharField()
    Email = CharField()
    register = DateTimeField(default = datetime.datetime.now)

    class Meta:
        database = db 