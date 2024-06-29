# Write a method that takes in a number and returns the number times two. Then run the method and print the result.

def get_double(number):
    return number * 2


print(get_double(8))

# Write a method that takes in a string and returns the string with all capital letters. Then run the method and print the result.


def string_to_uppercase(string):
    return string.upper()


print(string_to_uppercase("hello"))

# Write a method that takes in two numbers and returns the first number subtracted by the second. Then run the method and print the result.


def subtract_two_numbers(number1, number2):
    return number1 - number2


print(subtract_two_numbers(23, 4))

# Write a method that takes in a number and returns the number times itself. Then run the method and print the result.


def square_number(number):
    return number * number


print(square_number(8))

# Write a method that takes in a string and returns the first letter of the string. Then run the method and print the result.


def get_first_letter(string):
    return string[0]


print(get_first_letter("turbo"))

# Write a method that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the method and print the result.


def string_combiner(string1, string2, string3):
    return f"{string1} {string2} {string3}"


print(string_combiner("my", "name", "is"))

# Write a method that takes in a number and returns the number as a string. Then run the method and print the result.


def make_number_string(number):
    return str(number)


print(make_number_string(8))

# Write a method that takes in a string and returns the string repeated 5 times. Then run the method and print the result.


def string_repeater(string):
    return string * 5


print(string_repeater("hello"))

# Write a method that takes in 3 numbers and returns the average (the sum divided by 3.0). Then run the method and print the result.


def get_average(number1, number2, number3):
    return (number1 + number2 + number3) / 3


print(get_average(5, 6, 30))
