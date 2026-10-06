#In python modules and packages help organize and reuse code .Heres a comprehensive guide 
#on how to import them
from math import sqrt,pi
print(sqrt(16))
print(pi)
#Numpy is used because of speed ,less memory ,easier math.It allows you to perform calculations 
# on entire lists at once

#creating own custom packages and iimporting it
from packages.math import add
print(add(7,12))

from packages .math import * # '*' use star to import all the modules in packages 
print(subtract(10,3))
print(multiply(7,7))

#Standard library Overview
#Python Standard library  is vast collection of modules and packages that come 
#with python providing a wide range of functionalitiesout oof the box
#random
import random
print (random .randint(1,10))
print(random.choice(['apple','banana','cherry']))

#File and Directory Access
import os
print(os.getcwd())
#os.mkdir('test_dir')
#os.open('tst.txt')

#import shutil
#shutil.copyfile('source.txt','destination.txt')

#Data serialization 
#JSON:-Javascript Object Notation is a light weight format used for storing and 
# transporting data,mostly when data is sort from server to webpage

#To convert dict to Json by default json stored data in string
import json
data={'name':'krish','age':25}
json_str=json.dumps(data)
print(json_str)
print(type(json_str))

#now convert json data to its original datatype
parsed_data=json.loads(json_str)
print(parsed_data)
print(type(parsed_data))


'''Creating csv files and storing data in it'''

import csv
with open('example.csv',mode='w',newline='') as file:
    writer=csv.writer(file)
    writer.writerow(['name','age'])
    writer.writerow(['krish',32])

with open('example.csv',mode='r') as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)   

#datetime library
from datetime import datetime,timedelta
now =datetime.now()
print(now)

yesterday=now-timedelta(days=1)
print(yesterday) 

#time
import time
print(time.time())
time.sleep(2)
print(time.time())

##Regular Expression matching patterns
import re
pattern= r'\d+'
text='there are 123 apples 196'
match=re.search(pattern,text)
print(match.group())

import re

text = 'there are 123 apples 196'
pattern = r'\d+'

# This returns a list of all matches
numbers = re.findall(pattern, text)

print(numbers) 
# Output: ['123', '196']

#Conclusion:-Pythons standard library is extensive and provide tools for almost any task you
#can think of from file handling to web services from data serialization top concurrent execution.
#familirizing yourself with the moodules and packages available in the standard library can
#significantly enhance yoyr ability to write efficient and effective python proograms.
