# EXCEPTION HANDLING
#Example 1

#exception handling in python
#sytax error -wrong code
#runtime error - during program executon
#basic try except
#only test during development not during production
#during production the value must be analysed at initial point
try:
    print('inside try except block')
    num = int(input("Enter a number: "))
    print(10/num)
except ZeroDivisionError:
    print('division by zero')
except ValueError:
    print('invalid input. enter a number')



#Else and finally
#example 2
try:
    x = 10/2
except ZeroDivisionError:
    print("You can't divide by zero")
else:
    print("success",x)

finally:
    print("This always runs and works")


#Raising Exception
#Examle 3
#user defined exception to handle the error and provide more usability and flexibilty

def withdraw(balance,amount):
    if amount >= balance:
        raise Exception("You cannot withdraw more than you have")
    return balance - amount

withdraw = withdraw(100,100)
print(withdraw)


#custom  exception
#user defined exception to handle the error and provide more usability and flexibilty
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance,amount):
    if amount >= balance:
        raise InsufficientBalanceError("You cannot withdraw more than you have")
    return balance - amount

withdraw = withdraw(100,100)
print(withdraw)


# # Real life example 5
def login(username,password):
    if username != "admin":
        raise ValueError("user not found")
    if password != "123":
        raise ValueError("password incorrect")
    return "Into login"
try:
    print(login("asmi","123"))
except ValueError as e:
    print(e)



# #modules in python
# # Module: a file containing python codes to reuse
# #math_utitls.py
# from math_utils import add
#
# print(add(2,3))
#
#
#

























