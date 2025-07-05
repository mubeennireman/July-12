# Python program to find the factorial of a number provided by user.abs

'''userInput = int(input('Please enter a number:'))
factorial = 1
if (userInput < 0):
    print("Sorry factorial is not exist for negative number.")
else:
    for i in range (1, userInput + 1):
        factorial *= i
    print(f'Factorial of {userInput} is {factorial}')'''



# Write a program to print all Armstrong numbers in a given range. Note: An Armstrong number is a number whose sum of cubes of digits is equal to the number itself

armInput = int(input('please enter a number:'))
arm_remain = armInput
length = len(str(armInput))
sum = 0
while arm_remain != 0:
    reminder = arm_remain % 10
    reminder **= length
    sum += reminder
    arm_remain //= 10
if (sum == armInput):
    print(f'{armInput} is a Armstrong Number')
else:
    print(f'{armInput} isn\'t a Armstrong Number')

