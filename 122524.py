# Create an array to store 3 words. Then add two more words to the array and print the array on one line.

words = ["merry", "christmas", "ya"]
words.extend(["filthy", "animals"])
print(words)


# Create an array to store 4 letters. Then change the second letter to a number and print the array on one line.

array = ["a", "s", "d", "f"]
array[1] = 2
print(array)


# Create an array to store 5 numbers. Then print out each number on separate lines with a while loop.

numbers = [1, 2, 3, 4, 5]
index = 0
while index < len(numbers):
    print(numbers[index])
    index += 1


# Create an array to store 1 number. Then add three more numbers to the array and print the array on one line.

numbers1 = [1]
numbers1.extend([22, 55, 66])
print(numbers1)


# Create an array to store 3 strings with lower case letters. Then change the third string to have all capital letters and print the array on one line.

strings = ["ho", "ho", "ho"]
strings[2] = strings[2].upper()
print(strings)


# Create an array to store 3 names. Then print out each name on separate lines with a while loop.

names = ["santa", "rudolph", "herbie"]
index = 0
while index < len(names):
    print(names[index])
    index += 1


# Create an array to store 2 strings. Then add one string to the array and print the array on one line.

strings1 = ["milk", "cookies"]
strings1.extend(["chimney"])
print(strings1)


# Create an array to store 5 numbers. Then change the first number to 10 times its original value and print the array on one line.

numbers2 = [12, 25, 24, 12, 25]
numbers2[0] = numbers2[0] * 10
print(numbers2)


# Create an array to store 2 numbers. Then print out each number on separate lines with a while loop.
numbers3 = [12, 25]
index = 0
while index < len(numbers3):
    print(numbers[index])
    index += 1


# Create an array to store names of 3 different santas. Then add one more santa and print the array one line.

santas = ["Kris Kringle", "Santa Claus", "St. Nick"]
santas.extend(["Sinterklaas"])
print(santas)
