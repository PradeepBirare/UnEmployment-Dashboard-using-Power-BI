'''Lambda functions are small anonymousfunctions defined using the lambda keyword .
They can have any number of arguements but only one expression . They are commomnly used for short operation 
or as arguements to higher-order functions'''
#Syntax :- lambda arguments : expression
def addition (a,b):
    return a+b
print(addition (7,6))
print(type(addition))

#lambda function
add=lambda a,b: a+b
print(add(2,3))
print(type(add))

even1=lambda num: num%2==0
print(even1(2))

def addition2(x,y,z):
    return x+y+z
print(addition2(1,2,3))

add2=lambda a,b,c : a+b+c
print(add2(3,4,7))

#map applies a function to all items in a list
def square(number):
    return number**2

print(square(2))

numbers =[1,2,3,4,5,6]
square2=list(map(lambda x:x**2,numbers))
print(square2)

#definition :-The map function applies a given function to all items in an input list or
#any other iterable and returns a map object (an iterator ). 
# This is pareticularly useful for transforming data in alist comprehensievly
def square(x):
    return x*x
print(square(10))
numbers1=[1,2,3,4,5,6,7,8,9,10]
list1=list(map(square,numbers1))
print(list1)

#lambda with map function
numbers=[1,2,3,4,5,6,7,8]
added_number=list(map(lambda x,y : x+y ,list1,numbers))
print(added_number)

##use map to convert string to integers
str_numbers=['1','2','3','4','5','6']
int_numbers=list(map(int,str_numbers))
print(int_numbers)
print(type(int_numbers))

words=['apple','banana','cherry']
upperword=list(map(str.upper,words))
print(upperword)

def get_name(person):
    return person['name']

people=[{'name':'krish','age':25},
        {'name':'Jack','age':32}]
maplist=list(map(get_name,people))
print(maplist)

#Conclusion:-The map() function is a powerful tool  for applying transformations 
# to iterable data structures .It can be used with regular function,
#  lambda functions and even multiple iterables 
# ,providing a reusable approach to data processing in python

#filter() in python
#The filter function constructs an iterator from elements of an iterable for which a function 
#returns true .It is used to filter out items a list
#or any other iterables based on condition

def even(num):
    if num%2==0:
        return True
print(even(24))

lst =[1,2,3,4,5,6,7,8,9,10]
filterlst=list(filter(even,lst))
print(filterlst)

#using filter with lambda function
numbers=[1,2,3,4,5,6,7,8,9]
greater_than_five=list(filter(lambda x:x>5,numbers))
print(greater_than_five)

#filter with a lambda function and multiple conditions
numbers=[1,2,3,4,5,6,7,8,9,10]
even_and_greater_than_five=list(filter(lambda x: x>5 and x%2==0 ,numbers))
print(even_and_greater_than_five)

##filter to check if age is greater than 25 in dict
age_dict=[{'name':'krish','age':32
          },
          {'name':'jack','age':34},
           {'name':'john','age':25}]

def age(person):
    return person['age']>25
check_age=list(filter(age,age_dict))
print(check_age)
check_dict=list(filter(lambda x: x['age'] >25,age_dict))
print(check_dict)

#Conclusion:-The filter() function is a powerful tool for creating iterators
#that filter items out of an iterable based on a function .It is commomnly used for 
#data clleaning ,filtering objects and removing unwanted elements from lists .By 
#mastering filter you can write more concise and efficient code for processing and manipulating 
# collections in python

