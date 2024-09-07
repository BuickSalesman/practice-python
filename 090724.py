# Write a method that takes in a number and returns the number times two. Then run the method and print the result.


def get_double(number):
    return number * 2


print(get_double(3))

# Write a method that takes in a string and returns the string with all capital letters. Then run the method and print the result.


def uppercase(string):
    return string.upper()


print(uppercase("yo whaddup"))


# Write a method that takes in two numbers and returns the first number subtracted by the second. Then run the method and print the result.


def subtract_two_numbers(num1, num2):
    return num1 - num2


print(subtract_two_numbers(8, 3))


# Write a method that takes in a number and returns the number times itself. Then run the method and print the result.


def square_number(num):
    return num * num


print(square_number(9))


# Write a method that takes in a string and returns the first letter of the string. Then run the method and print the result.


def first_letter(string):
    return string[0]


print(first_letter("Yo whaddup"))


# Write a method that takes in three strings and returns a string that combines all three strings with spaces in between. Then run the method and print the result.


def string_combiner(str1, str2, str3):
    return str1 + " " + str2 + " " + str3


print(string_combiner("yo", "whaddup", "yo"))


# Write a method that takes in a number and returns the number as a string. Then run the method and print the result.


def stringify_number(number):
    return str(number)


print(stringify_number(88))


# Write a method that takes in a string and returns the string repeated 5 times. Then run the method and print the result.


def string_repeater(string):
    return string * 5


print(string_repeater("yo whaddup "))


# Write a method that takes in 3 numbers and returns the average(the sum divided by 3.0). Then run the method and print the result.


def average(*nums):
    total = sum(nums)
    return total / len(nums) if nums else 0


print(average(3, 3, 3, 5, 8, 2))


# Write a method that takes in a number and returns the number times 10 plus 30. Then run the method and print the result.


def do_math(number):
    return (number * 10) + 30


print(do_math(27))
