age=30
height=5.9
name="krish"

print("age",age)
print("height",height)
print("name",name)

''' understanding variable types'''
#Python is dynamically typed ,type of a variable is determined at runtime
age=25 #int
height=5.10#float
name="pradeep" #str
is_student=True #boolean

print('age:',age,type(age))
print('height:',height,type(height))
print('name:',name,type(name))
print('is_student',is_student,type(is_student))

#type checking and conversion
print(' **type checking and conversion **')
print(type(height))

age=36
print(age,'age',type(age))

#type conversion
print('After type conversion')
age_str=str(age)
print(age_str,'age',type(age_str))

age1 = input('enter an age ')
print(age1,type(age1)) #will give str 

#Simple calaculator
num1=int(input("enter num1:"))
num2=int(input("enter num2:"))

choice =int(input(
"1:add \n 2:Subtract \n 3:Multiply \n 4: Divide""\n "
"5:Floor division \n 6:Modulus\n"
"enter a choice:"))
if choice==1:
    print("add")
    sum=num1+num2
    print("add of two numbers:",sum)

elif choice==2:
    print("subtract")
    sum=num1-num2
    print("subtraction of two numbers:",sum)

elif choice==3:
    print("Multiply")
    sum=num1*num2
    print("Multiply of two numbers:",sum)  

elif choice==4:
    print("Divide")
    sum=num1/num2
    print("Divide of two numbers:",sum)      

elif choice==5:
    print("Floor Division")
    sum=num1//num2
    print("FLOOR Division of two numbers:",sum) 

elif choice==6:
    print("Modulus")
    sum=num1%num2
    print("Modulud of two numbers:",sum)        

