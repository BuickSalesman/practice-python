# Write a while loop to print the numbers 1 through 10.

number = 1
while number <= 10:
    print(number)
    number += 1

# Write a while loop that prints the word "hello" 5 times.

index = 1
while index <= 5:
    print("hello")
    index += 1

# Write a while loop that asks the user to enter a word and will run forever until the user enters the word "stop".

while True:
    word = input("Please enter a word: ")
    if word == "stop":
        break

# Write a while loop that prints the numbers 0 through 100, increasing by 5 each time.

index = 0
while index <= 100:
    print(index)
    index += 5

# Write a while loop that prints the number 9000 ten times.

index = 0
while index < 10:
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

count = 0
while count < 144:
    print("Around the world")
    count += 1

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
