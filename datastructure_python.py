#data strucutures in python

#1. list

mylist = [1,2.98,3,4,"python",True]
print(mylist[0])

mylist.append("coderush")   
print(mylist)

mylist.insert(2,"programming")
print(mylist)

mylist.remove(2.98)
print(mylist)

#loop through list
for item in mylist:
    print(item)

#2. tuple: it is an immutable list
gpsValues = (27.1212, 85.3232)
print(gpsValues[0])

#3. dictionary
intro = {"name":"jagriti", "age": 22, "city": "kathmandu"}
print(intro["name"])
intro["profession"] = "student"
print(intro)

# methods in dictionary
print(intro.get("profession"))
intro["age"] = 23
print(intro.get("age"))

del intro["city"]
print(intro)
intro.pop("profession")
print(intro)

for key in intro:
    print(key, intro[key])

#.keys() .values() .items()
for key, value in intro.items():
    print(key, value)


for key in intro.keys():
    print(key)
for value in intro.values():
    print(value)

#get() method
print(intro.get("name"))
#update() method
intro.update({"age": 24})
print(intro)
#clear() method
intro.clear()
print(intro)


#4.  set only unique values
print("ets ")
myset = {1,2,3,4,5}
print(myset)
myset.add(6)
print(myset)
myset.remove(3)
print(myset)    

list1 = [1,2,3,4,5,5]
print(list1)
myset_from_list = set(list1) 
print(myset_from_list)

#Differences between: list , dictionary  ,tuple,  set
#duplicate values in list. eg - shopping list 
#indexing in list and tuple
#key value pair in dictionary , example - student data in college 
#immutable in tuple , example - gps coordinates of a place
#unique values in set example - guest list in events