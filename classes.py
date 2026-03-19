
class FoodOrder:

    def __init__(self, customer_name, item, price):
        self.customer_name = customer_name
        self.item = item
        self.price = price

    def show_order(self):
        print("Customer: {}".format(self.customer_name))
        print("Item: {}".format(self.item))

person1 = FoodOrder("Asmita", "Pizza", 500)
person2 = FoodOrder("Ansu", "Momo", 200)
print(person1.customer_name, person1.item, person1.price)
print(person2.customer_name, person2.item, person2.price)
person1.show_order()
person2.show_order()


'''
# suppose you are working for daraz application and u have to work for new brand of laptop
# create a class Laptop with brand, price and method show_details() ,
'''

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_details(self):
        print("Brand: {}".format(self.brand))
        print("Price: {}".format(self.price))

daraz1 = Laptop("Daraz Laptop", 100000)
daraz1.show_details()













