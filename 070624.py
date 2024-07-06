# Write a program that uses a variable to store a number, then prints that number plus 10.

number = 2
print(number+10)

# Write a program that uses a variable to store a word, then prints that word with all capital letters.

word = "bird"
print(word.upper())

# Write a program that uses variables to store two numbers, then prints the numbers added together.

number1 = 2
number2 = 2

print(number1 + number2)

# Write a program that uses a variable to store a word, then prints that word in reverse order.

word = "bird"
print(word[::-1])

# Write a program that uses a variable to store a number, then prints the number times 10.

number = 5
print(number * 10)

# Write a program that uses variables to store two words, then prints both words on the same line in all capital letters.

word1 = "bird"
word2 = "word"
print(f"{word1} is the {word2}")

# Write a program that uses a variable to store a word, then prints the number of letters in the word.

word = "bird"
print(len(word))


# Write a program that uses a variable to store a number with decimals, then prints the number as an integer.

number = 9.89
print(int(number))


# Write a program that uses a variable to store two numbers, then prints the two numbers multiplied together.

number1 = 5
number2 = 8

print(number1 * number2)


# Write a program that uses a variable to store a word, then prints the word with all lowercase letters.

word = "BIRD"
print(word.lower())


# Use a variable to store a number, then write a condition that prints 0 if the number is equal to 10, and prints -1 otherwise.

number = 55
if number == 10:
    print(0)
else:
    print(-1)

# Use a variable to store a number, then write a condition that prints -1 if the number is less than 10, prints 1 if the number is greater than 10, and prints 0 if the number is equal to 10.

number = 92
if number < 10:
    print(-1)
elif number > 10:
    print(1)
else:
    print(0)

# Use variables to store two numbers, then write a condition that prints 1 if the numbers are both less than 10, and prints 0 otherwise.

number1 = 22
number2 = -9

if number1 < 10 and number2 < 10:
    print(1)
else:
    print(0)


# Use a variable to store a number, then write a condition that prints 1 if the number is over 9000, and prints -1 otherwise.

number = 76
if number > 9000:
    print(1)
else:
    print(-1)


# Use a variable to store a number, then write a condition that prints 9 if the number is less than 10, prints 19 if the number is less than 20, prints 29 if the number is less than 30, and prints -1 otherwise (only one print statement should occur).

number = 123
if number < 10:
    print(9)
elif number < 20:
    print(19)
elif number < 30:
    print(29)
else:
    print(-1)


# Use variables to store two numbers, then write a condition that prints 100 if either number is greater than 10, and prints -100 otherwise.

number1 = 23
number2 = -8
if number1 > 10 or number2 > 10:
    print(100)
else:
    print(-100)

# Use a variable to store a number, then write a condition that prints 1776 if the number is less than 0, and prints 1979 otherwise.

number = -2678
if number < 0:
    print(1776)
else:
    print(1979)


# Use a variable to store a number, then write a condition that prints 100 if the number equals 100, prints 99 if the number is equal to 99, and prints 0 otherwise.

number = 56
if number == 100:
    print(100)
elif number == 99:
    print(99)
else:
    print(0)

# Use variables to store two numbers, then write a condition that prints 1 if the first number is less than zero and the second number is greater than 0, and prints 0 otherwise.

number1 = 1
number2 = 2
if number1 < 0 and number2 > 0:
    print(1)
else:
    print(0)

# Use a variable to store a number, then write a condition that prints 5 if the number is greater than 80, prints 4 if the number is greater than 60, prints 3 if the number is greater than 40, prints 2 if the number is greater than 20, and prints 1 otherwise (only one print statement should occur).

number = 67
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
