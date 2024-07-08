# Create an array to store 3 words. Then add two more words to the array and print the array on one line.

instruments = ["guitar", "piano", "flute"]
instruments.extend(["bass", "theramin"])
print(instruments)

# Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.

letters = ["a", "b", "c", "d"]
letters[1] = 2
print(letters)

# Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.

numbers = [1, 22, 333, 44, 5]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1

# Create an array to store 1 number. Then add three more numbers to the array and print the array on one line.
numbers = [5]
numbers.extend([4, 77, -2])
print(numbers)


# Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.

fruits = ["apple", "banono", "cranburry"]
fruits[2] = fruits[2].upper()
print(fruits)


# Create an array to store 3 names. Then print out each name on separate lines with a while loop.

names = ["adam", "kelsey", "jakey"]
index = 0
while index < len(names):
    print(names[index])
    index += 1


# Create an array to store 2 strings. Then add one string to the array and print the array on one line.

foods = ["soup", "sandwich"]
foods.extend(["wellington"])
print(foods)


# Create an array to store 5 numbers. Then change the first number to 10 times its original value and print the array on one line.

numbers = [1, 2, 3, 4, 5]
numbers[0] = numbers[0] * 10
print(numbers)

# Create an array to store 2 numbers. Then print out each number on separate lines with a while loop.

numbers = [2, 3]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1


# Create an array to store names of 3 different countries. Then add one more country and print the array one line.

countries = ["istanbul", "egypt", "cuba"]
countries.extend(["japan"])
print(countries)
