from peewee import *
import datetime

db = SqliteDatabase('vendor_management.sqlite')
class BaseModel(Model):
    class Meta:
        database = db
#table for venues
class Show(BaseModel):
    show_venue = CharField()
    show_city = CharField()
    show_state = CharField()
    show_date = DateTimeField()

    def __str__(self):
        return f'Venue: {self.show_venue}   City: {self.show_city}  State: {self.show_state}    Date: {self.show_date}'

class Items(BaseModel):
    item_name = CharField()
    item_price = DecimalField()

    def __str__(self):
        return f'Item: {self.item_name}     Price: {self.item_price}'


class VenueSales(BaseModel):
    show_venue = CharField()
    item_name = CharField()
    qty_sold = IntegerField()

    def __str__(self):
        return f'Venue: {self.show_venue}   Item: {self.item_name}     Price: {self.qty_sold}'

db.connect()
db.create_tables([Show])
db.create_tables([Items])
db.create_tables([VenueSales])

def main():
    #loop will terminate if user selects '8'
    while True:

        print("1) Add Venue")
        print("2) Add Item")
        print("3) Add Sales")
        print("4) Show All Venues")
        print("5) Show All Items")
        print("6) Show All Sales")
        print("7) Show Most Sales For Specific Item")
        print("8) Exit")

        selection = input("Please Select:")
        if selection == '1':
            addVenue()
        elif selection == '2':
            addItem()
        elif selection == '3':
            addSales()
        elif selection == '4':
            showAllVenues()
        elif selection == '5':
            showAllItems()
        elif selection == '6':
            showAllSales()
        elif selection == '7':
            showMostSales()
        elif selection == '8':
            break
        else:
            print("Unknown Option Selected!")

def addVenue():
    enterVenue = input("Enter the name of the venue: ")
    enterCity = input("Enter the name of the city: ")
    enterState = input("Enter the name of the state: ")
    enterDay = int(input("Enter the date of the show: "))
    enterMonth = int(input("Enter the month of the show: "))
    enterYear = int(input("Enter the year of the show: "))
    # enterDay, enterMonth, and enterYear are passed as arguments to the datetime function.
    convertedDate = datetime.datetime(enterYear, enterMonth, enterDay)
    show = Show(show_venue=enterVenue, show_city=enterCity, show_state=enterState, show_date=convertedDate)
    show.save()

def addItem():
    enterItemName = input('Enter the name of the item')
    enterItemPrice = float(input('Enter the price of the item'))
    item = Items(item_name=enterItemName, item_price=enterItemPrice)
    #sales = IntegerField()
    #salesTable = Sales()
    #salesTable._meta.add_field(enterItemName, sales)
    #Sales.save()

    item.save()

def addSales():
    #venueExists = False
    while True:
        # enterVenue = input("Enter venue")
        # existing_venues = Show.select()
    #     for x in existing_venues:
    #         print(x)
    #         if enterVenue == x.show_venue:
    #             break
    #     print("Venue doesn\'t exist")
    #
    # while True:
    #     enterItemName = input('Enter the name of the item')
    #     for y in existing_items:
    #         print(y)
    #         if enterItemName == y.item_name:
    #             break
        enterVenue = input("Enter venue")
        enterItemName = input('Enter the name of the item')
        enterQty = int(input('Enter the quantity of x item sold'))
        existing_venues = Show.select()
        existing_items = Items.select(Items.item_name)

        for x in existing_venues:
            print(x)
            if enterVenue == x.show_venue:
                for y in existing_items:
                    print(y)
                    if enterItemName == y.item_name:
                        sales = VenueSales(show_venue=enterVenue, item_name=enterItemName, qty_sold=enterQty)
                        sales.save()
                        print("addition successful")
                        #success = True
                        break
        print("Error")
        # if success == True:
        #     print("PASSED")
        # else:
        #     print("FAIL")
                #else:
                    #print("ERROR ITEM")
                    #break
        #else:
            #print("ERROR VENUE")
            #break
    #adds sale to VenueSales

    #revenue = enterQty * itemPrice




def showAllVenues():
    allShows = Show.select()
    for show in allShows:
        print(show)

def showAllItems():
    allItems = Items.select()
    for item in allItems:
        print(item)

def showAllSales():
    allSales = VenueSales.select()
    for sale in allSales:
        print(sale)

def showMostSales():

    enterItemName = input("Enter the name of the item")
   # cond = ((VenueSales.item_name == enterItemName))
    sales = VenueSales.select(VenueSales, fn.MAX(VenueSales.qty_sold)).where(VenueSales.item_name == enterItemName)
    for sale in sales:
        print(sale)
main()