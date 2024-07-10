# Write a method that takes in a number and returns the number times two. Then run the method and print the result.

def double_number(number):
    return number * 2


print(double_number(8))

# Write a method that takes in a string and returns the string with all capital letters. Then run the method and print the result.


def uppercase_string(string):
    return string.upper()


print(uppercase_string("hello"))

# Write a method that takes in two numbers and returns the first number subtracted by the second. Then run the method and print the result.


def get_product(number1, number2):
    return number1 * number2


print(get_product(8, 9))

# Write a method that takes in a number and returns the number times itself. Then run the method and print the result.


def get_square(number):
    return number * number


print(get_square(9))


# Write a method that takes in a string and returns the first letter of the string. Then run the method and print the result.

def first_letter(string):
    return string[0]


print(first_letter("booyah"))


# Write a method that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the method and print the result.

def string_combiner(string1, string2, string3):
    return f"{string1} {string2} {string3}"


print(string_combiner("damn", "ass", "rock"))
# Write a method that takes in a number and returns the number as a string. Then run the method and print the result.


def number_to_string(number):
    return str(number)


print(number_to_string(8))
# Write a method that takes in a string and returns the string repeated 5 times. Then run the method and print the result.


def string_repeater(string):
    return string * 5


print(string_repeater("around the world "))


# Write a method that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the method and print the result.


def get_average(number1, number2, number3):
    return (number1 + number2 + number3) / 3


print(get_average(3, 4, 5))


# Write a method that takes in a number and returns the number times 10 plus 30. Then run the method and print the result.


def do_math(number):
    return (number * 10) + 30


print(do_math(8))
