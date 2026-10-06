#Introduction to function
#Definition:- A function is a block of code that performs a specific task .Functions helps in organizing
#code ,reusing code and improving readability

#Syntax:- def function name (parameter):
'''Docstring'''
#function  body
#return Expression

#Why Functions
num =24
if num%2 ==0:
    print("the number is even")
else :
    print("the number is odd") 

def even_or_odd(num):
    '''this function finds even or odd'''
    if num%2==0:
        print("the number is even:",num) 
    else:
        print("the number is odd:",num) 

#function with multiple parameters
def add(a,b):
    return a+b
result=add(2,4)
print(result)

#Default Parameters
def greet(name):
    print(f'hello {name},welcome to nirvana')

greet('krish')    

##Variable length Arguements
#Positional and keyword arguments
def print_numbers(*krish): #If it does not have a key name it becomes a positional arguments
    for number in krish:
        print (number)
print_numbers(1,2,3,4,5,6,7,8,"Krish")

##Positional arguements
def print_numbers(*args):
    for number in args:
        print(number)
print_numbers(1,2,3,4,5,6,7,8,"krish")

#keyword arguments
def print_details(**kwargs):
    for key,value in kwargs.items():
        print(f'{key}:{value}')
print_details(name="krish",age="32",country="India")

def print_details(*args,**kwargs):
    for val in args:
        print(f'Positional argument:{val}')

    for key,value in kwargs.items():
        print(f'{key}:{value}')
print_details(1,2,3,4,"krish",name="krsih",age="2",country="india")



##Return statements
def multiply(a,b):
    return a*b,a
print(multiply(2,3))

#Practical Examples Functions
#Example1 : temperature conversion
def convert_temperature(temp,unit):
    '''this function converts temperature between celsius and Fahrenheiit'''
    if unit=='C':
      return temp*9/5+32 #celsius to fahrenheit

    elif unit=='F':
        return (temp-32)*5/9# Fahrenheit to celsius
    else:
        return None
print(convert_temperature(25,'C'))
print(convert_temperature(77,'F'))

#Example 2 Password strength checker
def is_strong_password(password):
    """This function checks if the password is strong or not"""
    if len(password)<8:
       return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any (char.isupper() for char in password):
        return False
    if not any (char in '!@#$%&()_+' for char in password):
        return False
    else:
     return True
#calling password
print (is_strong_password("WeakPwd"))
print(is_strong_password("Str0NgPwD!"))    

#Example3 :- Calculate the total cost of item in a shopping cart

def calculate_total_cost(cart):
    total_cost= 0
    for item in cart:
        total_cost=total_cost+(item['price']*item['quantity'])
    return total_cost

    # cart data
cart=[
    {'name':'Apple','price':0.5,'quantity':4},
    {'name':'Banana','price':0.3,'quantity':6},
    {'name':'Orange','price':0.7,'quantity':3},

    ]    
total_cost=calculate_total_cost(cart)

print(total_cost)

#Example 4 check if a string is palindrome
def palindrome(s):
    s=s.lower().replace(" ","")
    if s==s[::-1]:
        print(f'{s} is palindrome {True}')
    else:
         print(f'{s} is not palindrome {False}')
palindrome("A man a plan a canal Panama")  
palindrome("hello")

#Example 5 Calculate the factorial of a number using recursion
def factorial(n):
    if n==0:
        return 1
    else:
        return n *factorial(n-1)
print(factorial(6))   

#Example6: A function to read a file and count the frequency of each word

def count_word_frequency(file_path):
    word_count={}
    with open(file_path,'r') as file:
        for line in file:
            words=line.split()
            for word in words:
                word=word.lower().strip('.,!?;:"\'')
                word_count[word]=word_count.get(word,0)+1
    return word_count
filepath='sample.txt' 
word_frquency=count_word_frequency(filepath)
print(word_frquency)

#example 7 validate email address
import re
#Email validation function
def is_valid_email(email):
    """This function checks if the email is valid"""
    pattern =r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match (pattern,email) is not None
# Calling the function
print(is_valid_email("test@example.com"))#output :True
print(is_valid_email("invalid-email")) #Output:false