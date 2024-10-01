# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

first_name = "kelsey"
last_name = "kavanagh"
full_name = first_name + " " + last_name
print(full_name)

# Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).

full_name = f"{first_name} {last_name}"
print(full_name)

# Write a program that asks the user to input a word. If the word is "marco", print "polo".

word = input("Please enter a word: ")
if word.lower() == "marco":
    print("polo")

# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation (the + operator).

color1 = "fish"
color2 = "car"
color3 = "flop"

print(
    "my favorite colors are " + color1 + ", " + color2 + ", and " + color3 + "."
)

# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).

print(f"my favorite colors are {color1}, {color2}, and {color3}.")

# Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."

name = input("Please enter your name: ")
if name != "Santa":
    print("Not Santa!")

# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation (the + operator).

title = "Plant Systematics"
author = "Michael G. Simpson"

print("the book is " + title + ", by " + author + ".")

# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation (the #{} operator).

print(f"the book is {title}, by {author}.")

# Write a program that asks the user to enter a password. If the password is "Joshua", the program responds "Shall we play a game?". For any other password, the program responds "Access denied"

password = input("Enter password: ")
if password == "Joshua":
    print("Shall we play a game?")
else:
    print("Access denied.")

# Write a program that uses variables to store the names of three cities, then prints out a sentence using that information with string concatenation (the + operator).

city1 = "poop town"
city2 = "butt city"
city3 = "pooperberg"

print(
    "my 3 fav places are " + city1 + ", " +
    city2 + ", and especially " + city3 + "!"
)
