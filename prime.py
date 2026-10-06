# Simple prime checker using a loop
'''num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is a prime number")
else:
    print(f"{num} is not prime")'''




# Simple program to print prime numbers from 1 to 100

n= int(input(" enetr the limit till print"))
for num in range(2, n):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
        print(num, end=" ")

