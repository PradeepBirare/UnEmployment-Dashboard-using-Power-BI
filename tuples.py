#TUPLES
#Tuples are built in datatype used to store items and can be duplicate values .it is ordered and 
# tuples denotes with round brackets()
empty_tuple=()
print(type(empty_tuple))

numbers=tuple((1,2,3,4,5,6))
print(numbers)

list1 =list((1,2,3,4,5,6))
print(list1)

mixed_tuple=(1,'hello',True,3.24)
print(mixed_tuple)

#Accesing tuple
print(numbers[2])
print(numbers[-1])


print(numbers[0:4])
print(numbers[::])

concattuple=(numbers)+(mixed_tuple)
print(type(concattuple))
print(concattuple)

#tuple methods

numbers1=tuple((1,2,3,4,5,6))
print(numbers1)
print (numbers1.count(4))
print(numbers1.index(3))

numbers2=(1,2,3,4,5,6)
print(numbers2.index(3))# index function tells the  element present at which index
nested_tuple=((1,2,3),('a','b','c'),(True,False))
print(nested_tuple[2])# accesing the nested elements through index

#iterating through nested tuples usinf for loop

for sub_tuple in nested_tuple:
    for item in sub_tuple:
        print(item,end=" ")
    print()    