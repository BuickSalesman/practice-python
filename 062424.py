# Use a variable to store a number, then write a condition that prints 0 if the number is equal to 10, and prints -1 otherwise.

number = 10

if number == 10:
    print(0)
else:
    print(-1)

# Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.

number = 11
if number < 10:
    print(-1)
elif number > 10:
    print(1)
else:
    print(0)

# Use variables to store two numbers, then write a condition that prints 1 if the numbers are both less than 10, and prints 0 otherwise.

number1 = 33
number2 = -2

if number1 < 10 and number2 < 10:
    print(1)
else:
    print(0)

# Use a variable to store a number, then write a condition that prints 1 if the number is over 9000, and prints -1 otherwise.

number = 1246322
if number > 9000:
    print("Over 9000!!")
else:
    print(-1)

# Use a variable to store a number, then write a condition that prints 9 if the number is less than 10, prints 19 if the number is less than 20, prints 29 if the number is less than 30, and prints -1 otherwise (only one print statement should occur).

number = 546

if number < 10:
    print(9)
elif number < 20:
    print(19)
elif number < 30:
    print(29)
else:
    print(-1)

# Use variables to store two numbers, then write a condition that prints 100 if either number is greater than 10, and prints -100 otherwise.

number1 = 11
number2 = 22

if number1 > 10 or number2 > 10:
    print(100)
else:
    print(-100)

# Use a variable to store a number, then write a condition that prints 1776 if the number is less than 0, and prints 1979 otherwise.

number = 56
if number < 0:
    print(1776)
else:
    print(1979)

# Use a variable to store a number, then write a condition that prints 100 if the number equals 100, prints 99 if the number is equal to 99, and prints 0 otherwise.

number = 7
if number == 100:
    print(100)
elif number == 99:
    print(99)
else:
    print(0)

# Use variables to store two numbers, then write a condition that prints 1 if the first number is less than zero and the second number is greater than 0, and prints 0 otherwise.

number1 = 22
number2 = 90

if number1 < 0 and number2 > 0:
    print(1)
else:
    print(0)

# Use a variable to store a number, then write a condition that prints 5 if the number is greater than 80, prints 4 if the number is greater than 60, prints 3 if the number is greater than 40, prints 2 if the number is greater than 20, and prints 1 otherwise (only one print statement should occur).

number = 45

if number > 80:
    print(5)
elif number > 60:
    print(4)
elif number > 40:
    print(3)
elif number > 20:
    print(2)
else:
    print(1)
