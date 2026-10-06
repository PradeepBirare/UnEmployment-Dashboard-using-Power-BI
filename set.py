#Sets they are nothing but built-in datatype in python used to store collection of unique items they are unordered
#cant allow duplicate values
my_set={1,2,3,4,5,9,10,16,20,13,14,15,17,18}
print(my_set)
print(type(my_set))

my_empty_set=set([1,2,3,46,7,8])
print(my_empty_set)
#sets operations
my_set.add(7)

my_set.add(6)
print(my_set)
my_set.remove(7)
print(my_set)   

my_set.discard(8)#Remove an element froma set if its a mmember

##pop method 
#my_set.pop() 
print(my_set)

#my_set.clear()
#print(my_set)

## Mathematical Operations
set1={1,2,3,4,5,6}
set2={4,5,6,7,8,9}

###Union
union_set=set1.union(set2) # will Take all unique values from the set

print(union_set)
#intersection
intersection_set=set1.intersection(set2) #will take only common or similar values from both sets
print(intersection_set)

newset=set1.difference(set2) #will remove common values from set1 by comparing both sets
print(newset)

newset2=set2.difference(set1) #will remove common values from set2 by comparing both sets
print(newset2)

newset3=set1.symmetric_difference(set2)#will print all  uniques values from both sets by removing similar values from the sets
print(newset3)

###Counting unique words in text

text="In this tutorial we are discussing about sets"
words=text.split()

##convert list of words to set to get unique words
unique_words=set(words)
print(len(unique_words))