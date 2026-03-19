# Inheritance + polymorphism Example
class Ride:
    def __init__(self, user,distance):
        self.user = user
        self.distance = distance

    def fare(self):
        print("The distance is:", self.distance)

class Bike(Ride):
    def __init__(self, user, distance):
        super().__init__(user,distance)

    def fare(self):
        print("The fare for",self.user," is:",  self.distance * 50)

class Car(Ride):
    def __init__(self, user, distance):
        super().__init__(user,distance)
    def fare(self):
        print("The fare for",self.user," is:", self.distance * 75)

user1 = Bike("Asmita",10)
user1.fare()
user2 = Car("Ansu",15)
user2.fare()
# Polymorphism: In this code, the method fare of class Ride is overriden by methods of child classes Bike and Car.
# It means, same name but different functionalities.



# Ecapsulation example
# It is used for protecting data, we cannot directly access it and change it.
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance # this is a private variable. self._balance is a protected variable

    def get_balance(self):
        return self.__balance
    def Deposit(self, amount):
        self.__balance += amount
        print(amount,"deposited successfully!")

    def Withdraw(self, amount):
        self.__balance -= amount
        print(amount,"withdrawn successfully!")

    def show_balance(self):
        print(self.__balance)

user1 = BankAccount(100000)
user1.show_balance()
user1.Deposit(1000)
user1.Withdraw(100)
user1.show_balance()
