# Python One-liners:

'''
Temporary assignment
'''
'''
Example 1
'''
a = 6
b = 9


a,b = b , a
print(f"a = {a}")
print(f"b = {b}")
a = 9
b = 6

If else:


'''
Example 2
'''
age = int(input("Enter your age: "))
print("Adult") if age >= 18 else print("Minor")

'''
Example 3
List comprehension:'''
squares = [i*i for i in range(1,6)]
print(squares)
[1, 4, 9, 16, 25]

evens = [i*i for i in range(20) if i % 2 == 0]
print(evens)
[1, 4, 9, 16, 25]


'''
Example 4
'''
text = "Asmita"
print(text[::-1])
atimsA

FIle one-liner:


data = open("text_file.txt").read()





data = open("text_file.txt").read()

#reverse list
numbers = [1, 2, 3, 4, 5]
print(numbers[::-1])

#check palindrome
is_palindrome = lambda s:s == s[::-1]
print(is_palindrome("madam"))


#count vowels in a string 
count = sum(c in 'aeiouAEIOU' for c in "Hello World")
print(count)


#remove vowels from a string
no_vowels = ''.join(c  for c in "hello world" if c.lower() not in 'aeiou')
print(no_vowels)


#capitalize first letter of each word
capitalized = ' '.join(word.capitalize() for word in "hello world".split())
print(capitalized)


#calculate factorial
from math import prod;
factorial = lambda n: prod(range(1,n+1))
print(factorial(5))

#check if a number is prime
is_prime = lambda n: n > 1 and all(n % i for i in range(2, int(n**0.5) + 1))
print(is_prime(7))

#generate Fibonacci sequence
fib = lambda n: [0,1][:n]+ [sum([0,1][:n][-2:]) for _ in range(n-2)]
print(fib(10))


#get gcd of two numbers
from math import gcd
result = gcd(48, 18)
print(result)

# #sum of squares from 1 to n
sum_sq = sum(i*i for i in range(1, 11))
print(sum_sq)

# #Ternary conditional 
x = 5
result = "Yes" if x > 1 else "No"
print(result)


#check uniqueness
unique = len(set([1, 2, 3, 4, 4])) == len([1, 2, 3, 4, 5])
print(unique)

#check if two strings are anagrams
are_anagrams = lambda s1, s2: sorted(s1) == sorted(s2)
print(are_anagrams("listen", "silent"))

#list
list1 = [1, 2, 3]
list2 = [3, 2, 1]
are_anagrams = sorted(list1) == sorted(list2)
print(are_anagrams)


#get the most frequent element
lst = [1, 2, 3, 4, 4, 5]
most_frequent = max(set(lst), key=lst.count)
print(most_frequent)


#remove none values 
lst = [1, None, 2, None, 3]
cleaned = [x for x in lst if x is not None]
print(cleaned)



'''Data Structures and collections'''
#Example 1
from collections import Counter
counts = Counter(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])
print(counts)

#Sot the dictionary by value

sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
print(sorted_counts)

#merge two dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
print(merged)


#invert a boolen list
bool_list = [True, False, True, False]
inverted = [not x for x in bool_list]
print(inverted)


#group list by even and odd
lst = [1, 2, 3, 4, 5, 6]
groups = {'even': [x for x in lst if x%2 == 0], 'odd': [x for x in lst if x%2 != 0]}
print(groups)

#find common elements in 3 lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
list3 = [4, 5, 6, 7]
common = set(list1) & set(list2) & set(list3)

print(common)

#convert binary to decimal
binary_str = "1011"
decimal = int(binary_str, 2)
print(decimal)

#find second largest number
second_largest = sorted(set([1, 2, 3, 4, 5]))[-2]
print(second_largest)

#unpack a tuple into variables
a,b,c = (1, 2, 3)
print(a, b, c)

#find length of longest word in a list
words = ["hello", "world", "python", "programming"]
max_len = max(map(len, words))
print(max_len)


#print elements of a list without brackets
print(*[1, 2, 3, 4, 5], sep=', ')

#repeat string n times
s = "hello"
repeated = s * 3
print(repeated)





















