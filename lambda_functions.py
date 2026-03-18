# lambda function is a small, one line anonymous function that can take any number of arguments but can only have one expression. It is defined using the lambda keyword.
#it is useful when you need a small function for a short period of time 
# syntax: lambda arguments: expression

# Example 1: A lambda function that adds two numbers
add = lambda x,y: x+y
print(add(5,3))

# Example 2: A lambda function that squares a number
square = lambda x: x **2 
print(square(4))

#using enumerate
numbers = [1,2,3,4,5]
for i,num in enumerate(numbers):
    print(f"Index: {i}, Number: {num}")

# Sorting functions
nums = [5,2,9,1,5,6]
print(sorted(nums)) #sorts array and returns a new sorted array
print(nums) #original array remains unchanged

print(sorted(nums, reverse=True)) #sorts in descending order
print(nums) #original array remains unchanged

nums.sort() #sorts the original array in place
print(nums) #original array is now sorted


#sorting by a specific key
students =  [("Ram", 20), ("Shyam", 18), ("Hari", 22)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students) #sorts students by age

#filter function : used to filter elements based on a condition
# syntax: filter(function, iterable)

numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = list(filter(lambda x: x %2 ==0,numbers))
print(even_numbers) #filters out even numbers from the list

#map function: used to apply a function to all items in an iterable
# syntax: map(function, iterable)

numbers = [1,2,3,4,5]
squared = list(map(lambda x: x**2, numbers))
print(squared) #squares each number in the list

#multiple iterables 
a = [1,2,3]
b = [4,5,6]
result = list(map(lambda x,y: x+y, a,b))
print(result) #adds corresponding elements from both lists

names = ["Alice", "Bob", "Charlie"]
uppercase_names = list(map(lambda x: x.upper(), names))
print(uppercase_names)

#filter students who passed
students = [("Alice", 85), ("Bob", 60), ("Charlie", 45)]
# passed_students = list(filter(lambda x: x[1]>=60, students)) OR
passed_students = list(filter(lambda x: x["marks"]>=60, students))
print(passed_students)

# lambda with multiple conditions
check = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(4))

check_positive = lambda x: "Positive" if x > 0 else "Negative"
print(check_positive(5))
print(check_positive(-3))

#lambda returning multiple values 
calc = lambda x: (x, x**2, x**3)
print(calc(3))


#nested lambda functions
multiply = lambda x: lambda y: x*y 
result = multiply(5)(4)
print(result) #returns 20
