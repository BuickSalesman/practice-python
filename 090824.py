# Write a while loop to print the numbers 1 through 10.

number = 1

while True:
    print(number)
    number += 1
    if number > 10:
        break
    # i know this is a stupid way to do this


# Write a while loop that prints the word "hello" 5 times.

number = 0

while number < 5:
    print("hello")
    number += 1


# Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".

while True:
    word = input("Enter a word: ")
    if word == "stop":
        break


# Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.

index = 0

while index <= 100:
    print(index)
    index += 5


# Write a while loop that prints the number 9000 ten times.

index = 0

while index < 5:
    print(9000)
    index += 1


# Write a while loop that asks the user to enter a number and will run forever until the user enters a number greater than 10.

while True:
    number = input("Please enter a number: ")
    if int(number) > 10:
        break


# Write a while loop that prints the numbers 50 to 70.

number = 50

while number <= 70:
    print(number)
    number += 1


# Write a while loop that prints the phrase "Around the world" 144 times.

index = 1

while index <= 144:
    print(f" {index}. Around the world")
    index += 1


# Write a while loop that asks the user to enter a word and will run forever until the user enters a word with more than 5 letters.

while True:
    word = input("Please enter a word: ")
    if len(word) > 5:
        break


# Write a while loop that prints the even numbers from 2 to 40.

index = 2

while index <= 40:
    print(index)
    index += 2


# Create an array to store 3 words. Then add two more words to the array and print the array on one line.

words = ["my", "name", "is"]
words.append("slim")
words.append("shady")

print(words)


# Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.

letters = ["a", "b", "c", "d"]
letters[1] = 2

print(letters)


# Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.

numbers = [1, 2, 3, 4, 5]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1


# Create an array to store 1 number. Then add three more numbers to the array and print the array on one line.

numbers = [1]
numbers.extend([2, 3, 4])

print(numbers)


# Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.

strings = ["any", "grey", "poupon"]
strings[2] = strings[2].upper()

print(strings)


# Create an array to store 3 names. Then print out each name on separate lines with a while loop.

names = ["Adam", "Kelsey", "Jakey"]
index = 0

while index < len(names):
    print(names[index])
    index += 1


# Create an array to store 2 strings. Then add one string to the array and print the array on one line.

strings = ["poop", "scoop"]
strings.append("droop")

print(strings)


# Create an array to store 5 numbers. Then change the first number to 10 times its original value and print the array on one line.

numbers = [1, 2, 3, 4, 5]
numbers[0] *= 10

print(numbers)


# Create an array to store 2 numbers. Then print out each number on separate lines with a while loop.

numbers = [33, 65]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1
