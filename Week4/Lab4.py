# Lab3
# Author: Alejandro Canas
# Lab4
# Author: Alejandro Canas

"""_summary_
This lab is designed to get you familiar with Python Boolean Expressions, Conditional Expressions, if-elif-else statements, and while / for loops.
"""

# 1. Write some code that asks the user for a number and prints out whether it is positive, negative, or zero.
NumberInput = input("type in a number please: ")

print(NumberInput)
if NumberInput > "0":
    print("Yay its a positive number")
elif NumberInput < "0":
    print("Boo its a negative number")
else:
    print("Boring its a zero")

# 2. Write some code that asks the user for a number and prints out whether it is even or odd.
NumberInput = input("type in a number please: ")

print(NumberInput)
if int(NumberInput) % 2 == 0:
    print("Yay its a even number")
else:
    print("Boo its an odd number")
# 3. Write some code that asks the user for a number and prints out all the numbers from 1 to that number using a while loop.
askNumber = input("Type in any number: ")
i = 0
while i != int(askNumber):
    i = i+1
    print(i)
print('Done!')

# 4. Use a for loop to ask a user for 5 numbers and print out the average of those 5 numbers.
i = 1
sum = 0
for i in range (5):
    askloopnumber = input("Type in any number: ")
    print (int(askloopnumber))
    sum += int(askloopnumber)
average = sum/5
print(average)
# 5. Write some code that prints out all the numbers from 1 to 10 that are divisible by 3 or 5.

for i in range(1,11):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
# 6. Write some code that asks the user for a number and then prints out a countdown from that number to 1 using a while loop. After the countdown, print "Blast off!".
blastnumber = int(input("enter a number please: "))
counter = blastnumber
while counter >= 1:
    import time
    time.sleep(1)
    print(counter)
    counter = counter - 1
print("blast off!")
# 7. Write some code that asks the user for a number and then uses a for loop to iterate from 1 to that number. If the current number is divisible by 7, print "Lucky" and continue to the next iteration. If the current number is greater than 100, break the loop.
luckynumber = int(input("Enter a number: "))
for i in range(1, luckynumber+1):
    if i % 7 ==0:
        print("Lucky this time")
    if i > 100:
        break
    print(i)