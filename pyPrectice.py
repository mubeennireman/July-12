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

'''armInput = int(input('please enter a number:'))
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
    print(f'{armInput} isn\'t a Armstrong Number')'''


# write a program to multiply two numbers by repeated addition.abs

'''Input_1 = int(input('Enter first number:'))
Input_2 = int(input('Enter second number:'))
sum = 0
for i in range(1, Input_2 + 1):
    sum += Input_1
print(f'Both numbers multiple is {sum}')'''



#  write a program which takes list of numbers as input and finds:
#  1. the large number in list      2. the smallest number in the list      3. product of all the item in the list

'''list_ = []
multiply_item = 1
count_item = int(input('how many item you want in list? :'))
if (count_item < 0):
    print('invalid number!')
elif (count_item == 0):
    print('list doesn\'t have item')
else:
    for i in range(1, count_item + 1):
        list_item = int(input('enter item:'))
        multiply_item *= list_item
        list_.append(list_item)
    print(f'list  is:{list_}')
    print(f'large number of list is :{max(list_)}')
    print(f'small number of list is :{min(list_)}')
    print(f'list item multiply is :{multiply_item}')'''