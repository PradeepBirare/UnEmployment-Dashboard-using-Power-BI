#nested

## determine if a year is a leap year using nested condition statements

'''year=int(input("enter a year to check if leap year: "))

if year%4==0:
    if year%100==0:
        if year%400==0:
            print({year},"year is leap year")
        else :
            print(year,"not a leap year") 
    else:
        print(year,"is a leap year")               
else:
    print("not a leap year")    


#Determine the ticket price using age and student

age = int(input("enter the age"))

is_student = input("if student yes or no").lower()

if age < 5 :
    price="free"
    

    print("age is ",age ,"then price:",price)

elif age <=12:
    price ='10$'
    

    print("age is ",age ,"then price:",price)
elif age <= 17:
    if is_student =='yes':
        price ="$12"
         
        print("age is ",age ,"then price:",price)
    else :
        price ='$18'


elif age <= 64:
    if is_student== 'yes':
      price ="$16" 
      print("age is ",age ,"then price:",price)  
    else:
      price=('$18')

elif age >= 70:
      if is_student == 'no' or is_student == 'no':
          price = "$5"
      
      print("age is ",age ,"then price:",price)
else:
      price = '$18'

print("age is ",age ,"then price:",price) '''

# for loop
a=range(10)
for i in a:
   print(i)   
# step last no will be skipped (start,stop,step)
b=range(1,10)
print(b)
for i in b:
    print (i)   


#strings  
str2="hello world"
for i in str2 :
    print(i)   
print(len(str2))   

# The while loop continues to execute as long as the conition is true 
count=0
while count< 5:
    count=count+1
    print (count)    

#loop controlled statements
# break statement
##The break statement is used to exit a loop prematurely when a certain condition is met. When the break statement is encountered, the loop terminates immediately, and the program continues with the next statement after the loop.

for i in range(1,10):
    if i==5:
        #print(i)
        break
    print(i)


# continue statement
#continue statement is used to skip the current iteration of a loop and move to the next iteration. When the continue statement is encountered, the rest of the code inside the loop for that iteration is skipped, and the loop proceeds with the next iteration.      

for i in range(1,10):
    if i%2 == 0:
        continue
    print('odd number is ',i)

for i in range(1,10):
    if i==5:    
       continue
    print(i)
    
#pass statement
#the pass statement is a placeholder that does nothing. 
# It is used when a statement is syntactically required 
# but you don't want to execute any code. 
# It allows you to create empty blocks of code without causing syntax errors.

for i in range(1,10):
 if i==5:
     pass
 print(i)


#nested loops
for i in range(3):
    for j in range(2):
        #print("i:",i,"j:",j)
        print(f"i:{i},j:{j}")


## Examples calculate the sum of the first n natural numbers using a for loop and while loop

n=10
sum=0
count=1
while count<=n:
    sum=sum+count
    print("how sum is adding",sum)
    count=count+1
    print("how count is adding ",count)
print("the sum of first n natural numbers is ",sum)

 
 #for loop
n=10
sum=0
for i in range(11):
    sum=sum+i
    print("how sum is adding",sum)

## prime no examples
num=int(input("enter a no till  how much number to print prime no: ")) 

for num in range(1,num):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num,"is a prime number") 