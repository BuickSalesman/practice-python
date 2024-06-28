# Create an array to store 3 words. Then add two more words to the array and print the array on one line.

words = ["apple", "banana", "jeff"]

words += ["kelsey", "adam"]

print(words)

# Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.

letters = ["a", "b", "c", "d"]
letters[1] = 2
print(letters)

# Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.

numbers = [1, 3, 5, 7, 9]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1

# Create an array to store 1 number. Then add three more numbers to the array and print the array on one line.

numbers = [1]
numbers += [2, 3, 4]
print(numbers)

# Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.

names = ["adam", "jeff", "kelsey"]
names[2] = names[2].upper()
print(names)

# Create an array to store 3 names. Then print out each name on separate lines with a while loop.

names = ["adam", "kelsey", "jeff"]
index = 0
while index < len(names):
    print(names[index])
    index += 1

# Create an array to store 2 strings. Then add one string to the array and print the array on one line.

names = ["adam", "kelsey"]
names += ["jeff"]
print(names)

# Create an array to store 5 numbers. Then change the first number to 10 times its original value and print the array on one line.

numbers = [1, 2, 3, 4, 5]
numbers[0] = numbers[0] * 10
print(numbers)

# Create an array to store 2 numbers. Then print out each number on separate lines with a while loop.

numbers = [22, 44]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1

# Create an array to store names of 3 different countries. Then add one more country and print the array one line.

countries = ["armenia", "afghanistan", "egypt"]
countries += ["france"]
print(countries)
