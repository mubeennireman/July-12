# Python program to find the factorial of a number provided by user.abs

userInput = int(input('Please enter a number..'))
factorial = 1
if (userInput < 0):
    print("Sorry factorial is not exist for negative number.")
else:
    for i in range (1, userInput + 1):
        factorial *= i
    print(f'Factorial of {userInput} is {factorial}')



# 