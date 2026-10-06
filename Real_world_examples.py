#Example 1 :- Manage a todo list
to_do_list=['buying the groceries','clean the house','Pay bills']
#Adding task in list
to_do_list.append("Schedule Meeting")
to_do_list.append("go for a run")
#Removing a completed task
to_do_list.remove("clean the house")

##Checking if a task is in the list
if 'Pay bills ' in to_do_list:
    print("Dont forget to pay utility bills")
print('to_do_list remaining')
for task in to_do_list:
    print(f"{task}")    


#Example 2 :- Organizing students grade
grades=[85,92,78,90,88]

grades.append(95)
#calculating the average grades
average_grades=sum(grades)/len(grades)
print("Average grades",average_grades)

#finding the highest and lowest grades

highest_grades=max(grades)
lowest_grades=min(grades)
print(f'highest grades:{highest_grades}')
print(f'lowest grades:{lowest_grades}')


#Example3 :-Use a list to manage inventory items of a store
inventory=['mango','kiwi','banana','orange']

inventory.append('dragonfruit')

item='orange'
if item in inventory:
    print(f'{item} in stock')
else:
    print(f'{item} out of stock') 

print ("Inventory list:")
for item in inventory:
    print(f"- {item}")   

 #example 4 : Collecting user feedback using list and analyze it

feedback=['Great service','Very satisfied','Could be better','Excellent experience']

feedback.append('Not happy with the service')

#Counting specific feedback

positive_feedback_count=sum(1 for comment in feedback if "great" in comment.lower() or \
 "excellent" in comment.lower())
  
print(f'Positive feedback count:{positive_feedback_count}')
#Printing all feedback
print("user feedback")
for comment in feedback:
    print(f"{comment}")