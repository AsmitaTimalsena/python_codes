# Example 1
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
#
#Example 2
# '''
# # suppose you are working for daraz application and u have to work for new brand of laptop
# # create a class Laptop with brand, price and method show_details() ,
# '''

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
    def show_details(self):
        print("Brand: {}".format(self.brand))
        print("Price: {}".format(self.price))

daraz1 = Laptop("Daraz Laptop", 100000)
daraz1.show_details()


#Example 3
class Restaurant:
    menu = {
        "Pizza": 500,
        "Burger":600,
        "Pasta":400,
        "Salad": 300,
        "Ice cream": 200
    }

    def __init__(self, customer_name):
        # Object attributes
        self.customer_name = customer_name
        self.order = []
        self.order_summary = {}
        self.discount = 0

    def place_order(self,item,quantity):
        if item in Restaurant.menu:
            price = Restaurant.menu[item] * quantity
            order = (item,quantity,price)
            self.order.append(order)
            self.order_summary[item] = self.order_summary.get(item,0)+quantity
            print(f"{self.customer_name} ordered {quantity}x{item}")
            print("Order placed successfully")
        else:
            print(f"Sorry, {item} is not in the menu.")

    def apply_discount(self,percent):
        self.discount = percent
        print(f"A discount of {percent}% has been applied for {self.customer_name}.")

    def calculate_total(self):
        total_func = lambda order: order[2] #this func gets price
        total = sum(total_func(order) for order in self.order) #loop+sum
        if self.discount>0:
            total = total-(total * self.discount/100) #applying discount
        return total
    def unique_items_ordered(self):
        return set(item[0] for item in self.order)

    def show_summary(self):
        print("\n---------Order Summary---------\n")
        print("Item-wise quantity (dictionary):", self.order_summary)
        print("Unique items ordered (set):",self.unique_items_ordered())
        print("Discount applied: ",self.discount,"%")
        print("Total bill after discount: ",self.calculate_total(),"INR")
        print("--------------\n-------------")

customer1 = Restaurant("Asmita")
customer1.place_order("Pizza",5)
customer1.place_order("Ice Cream",2)
customer1.apply_discount(5)
customer1.show_summary()
customer2 = Restaurant("Ansu")
customer2.place_order("Burger",2)
customer2.apply_discount(2)
customer2.show_summary()










































