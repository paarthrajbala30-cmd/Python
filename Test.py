

values = (10, 20, 30, 40)
for x in values:
    print(x)
     
print(10 in[1, 2, 3, 4])

#program to print your name nine times using for loop with range() function.
name = input("Enter your name : ")
for i in range(9):
    print(name)
'''
for i in range(5) :
    if i == 2:
        continue
    print(i)
print('Out of loop and 2 is skiped')
'''
#Program to print all the days of the week 

'''
#program to print multiplicatiion table of an input number.

number = int(input("enter a number: "))
for i in range(1, 11):
    print(f"{number} X (i) = {number * i}")
'''

#muliplication of a given table using while loop 


number = int(input("enter a number: "))
i=1
while i <= 10:
    print(f"{number} x {i} = {number * i}")
    i += 1

# program to demonstrate the uesnof while loop with else statement.

i = 1 # Initailize the variable i
while i <= 5:
    print(i)
    i += 1
else:
    print('The while loop ends here')
'''
while (1):

    print ("hello")
'''
'''
for i in range(12):
    if i == 7:
        break
    print(i)
    print('out of loop')
 '''
x = 1
while i <= 10:
    print(i)
    i = i + 1

def greet(name):
    print("hello", name, "!")

def add_number(a, b):
    return a + b

# Correct usage:
greet