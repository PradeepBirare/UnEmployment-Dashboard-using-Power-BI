#List are built in datatype used to store items and can be duplicate values .it is ordered and l
# ist denotes with square brackets[]
# list of items creation

lst=[1,2,3,4]
print(lst)
print(type(lst))

lst2=[1,2.5,'hello',True]
print(lst2)

#Accessing list items
lst3=['apple','banana','cherry ','date','fig','grape']
print(lst3[0])#apple
print(lst3[3])# date
print(lst3[-4])#cherry
print(lst3[3:-1])#will skip last element
print(lst3[1:])
print(lst3[:-3]) #will, take elemets from beginning when : is at the start
print(lst3[-4:])#will take elements from the end when : is at the end
lst3[0]='avocado'
print(lst3)
lst3.append('kiwi')# will append/add element at the end of the list
print(lst3)
lst3.insert(6,'mango')# will insert element at the specified index
print(lst3)
lst3[7]='orange' # will change the element at the specified index
print(lst3)
lst3.remove('mango')# will remove the mentioned specified value
print(lst3)
lst3.pop(4)#will remove the element at the specified index and return it
print(lst3)
del lst3[2]# will delete the element at the specified index
print(lst3)
lst3.sort()# will sort the list in ascending order
print(lst3)
lst3.reverse()# will reverse the order of the list
print(lst3)

str4="mango"
print(str4[::-1])


#slicing of list
numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers[2:5]) #[3,4,5]
print(numbers[::2])#[1,3,5,7,9] will skip every second element
print(numbers[:5])#[1,2,3,4,5]
print(numbers[5:])#[6,7,8,9,10]
print(numbers[::-1])#[10,9,8,7,6,5,4,3,2,1]

# iterating with index 
for index,number in enumerate(numbers):
    print(index,number)


#list comprehension
lst4=[]
for x in range(10):
    lst4.append(x**2)
print(lst4)    


lst5 =[x**2 for x in range(10)]
print(lst5)

#list comprehension syntax [expression for item in iterable]
#with conditional logic [expression for item in iterable if condition]

even=[]

for i in range(10):
    if i%2==0:
     even.append(i)
print(even)

odd_number=[num for num in range(10) if num%2!=0]
print (odd_number)

#Nested list comprehension
#[expression for item1 in iterable1 for item2 in iterable2]

words=['hello','world','python','list']
lengths=[len(word) for word in words ]
print(lengths)