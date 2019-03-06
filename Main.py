from peewee import *
import sqlite3
#specify product name
#specify quanitity sold

db = SqliteDatabase('vendor_management.sqlite')

class VendorItems(Model):
    item_name = CharField()


    class Meta:
        database = db
class Show(Model):
    show_venue = CharField()
    show_city = CharField()
    show_state = CharField()

class Sales(Model):
    show_venue = CharField()
    item_name = CharField()
    qty_sold = IntegerField()


db.connect()
db.create_tables([VendorItems])
#db.create_tables([Show])
def main():

    while True:

        print("1) Add Contestant")
        selection = input("Please Select:")
        if selection == '1':
            break