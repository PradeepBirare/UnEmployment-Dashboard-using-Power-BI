#dictionaries are unordered collection of items They store data in key_value pairs .
# key must be unique and immutable and values are mutable
# 

#creating dictionaris
empty_dict ={}
print(type(empty_dict))

empty_dict1=dict({1:2,2:'hello','name':'pradeep'})
print(type(empty_dict1))
print(empty_dict1)

student={'name':'john','age':'30','grade':'A'}
print(student)

#if you store duplicate values in dictionary it will show only the new stored duplicated value
#example:-  
student={'name':'john','age':'30','grade':'A','name':'krish'}
print(student)
#output :- {'name': 'krish', 'age': '30', 'grade': 'A'}


##Accessing Dictionary Elements
student={'name':'Krish','age':'30','grade':'A'}
print(student['name']) #output  Krish
print(student.keys())  #output   dict_keys(['name', 'age', 'grade'])
print(student.values()) #output  dict_values(['Krish', '30', 'A'])

#Accessing using get() method
print(student.get('grade'))
print(student.get('name'))
print(student.get('age'))

#even if you use get method for undefined or not their key value pair in the dictionary
#  it will still give some result i.e none
#example
print(student.get('last_name'))# output : None
#another  method to use get() we can store temporary values in the diictionary 
print(student.get("last_name","Hero"))
#o/p :- hero 
#but in our main dictionary no changes has happened 
print(student) #o/p {'name': 'Krish', 'age': '30', 'grade': 'A'}


#Modifiying dict elements

student['age']=32
print(student)
student['address']='Bandra'
print(student)
#output:- {'name': 'Krish', 'age': 32, 'grade': 'A', 'address': 'Bandra'}

#deleting elements in dict
del student['grade']
print(student)
#o/p:- {'name': 'Krish', 'age': 32, 'address': 'Bandra'}

#Dictionary methods
keys=student.keys()
print(keys)
#gett all keys dict_keys(['name', 'age', 'address'])

values=student.values()
print(values)
#get all values dict_values(['Krish', 32, 'Bandra'])

#shallow copy
student_copy=student
print(student_copy)
#if make changes in main dictionary shallow copy dict will also change
student['name']='Thor'
print(student_copy)

#now copying using copy()
student_copy1=student.copy()
print(student_copy1)
# using copy() method if we do changes in main dict the copy dict will 
# dont have that changes
student['name']='Hercules'
print(student_copy1)
#output:-{'name': 'Thor', 'age': 32, 'address': 'Bandra'}
#Iterating over dictionaries you can use loops to iterate over 
# dictionaries , keys , values or items
#Iterate over key
for keys in student.keys():
    print(keys)
#result :-
# name
# age
# address

#Iterate over values
for values in student.values():
    print(values)

#result:
# Hercules
# 32
# Bandra


#iterate over key value pairs
for keys,values in student.items():
    print(f'{keys}:{values}')
#result
# name:Hercules
# age:32
# address:Bandra

#Nested dict
students={
 
    "student1":{'name':'Steve','age':32},
    "student2":{'name':'Peter','age':26}

}
print (students)

#Accessing nested dictionaries elements

print(students['student1']['name'])
print(students['student2']['name']) 

##Iterating over nested dictionaries
for student_id ,student_info in students.items():
    print(f'{student_id}:{student_info}')
    for keys,values in student_info.items():
        print(f'{keys}:{values}')


 #{'student1': {'name': 'Steve', 'age': 32}, 'student2': {'name': 'Peter', 'age': 26}}
#Steve
#Peter
#student1:{'name': 'Steve', 'age': 32}
#name:Steve
#age:32
#student2:{'name': 'Peter', 'age': 26}
#name:Peter
#age:26       

#Dictionary Comprehension
square={x:x**2 for x in range(5)}
print(square)
#output:-{0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

#condition dictionary comprehension
evens={x:x**2 for x in range(10) if x%2==0}
print(evens)
#output:-{0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

##Practical Examples
#Use a dictionary to count the frequency of elements in list

        







numbers=[1,2,2,3,3,3,4,4,4,4]
frequency={}
for number in numbers:
    if number in frequency:
     frequency[number]+=1
    else:
        frequency[number]=1
print(frequency)  

##Merge 2 dictionaries into one
dict1={"a":1,"b":2}
dict2={"b":3,"c":4}
merged_dict={**dict1,**dict2}
print(merged_dict)
#result:-{'a': 1, 'b': 3, 'c': 4}