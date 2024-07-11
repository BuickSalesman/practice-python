# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

first_name = "Kelsey"
last_name = "Kavanagh"
print(first_name + " " + last_name)

# Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).
first_name = "Kelsey"
last_name = "Kavanagh"

print(f"{first_name} {last_name}")

# Write a program that asks the user to input a word. If the word is "marco", print "polo".

word = input("Please enter a word: ")
if word == "marco":
    print("polo")

# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation (the + operator).

color1 = "red"
color2 = "blue"
color3 = "green"

print("My favorite colors are " + color1 +
      ", " + color2 + ", and " + color3 + ".")


# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).

color1 = "red"
color2 = "blue"
color3 = "green"

print(f"My favorite colors are {color1}, {color2}, and {color3}.")

# Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."

name = input("Please enter your name: ")
if name != "Santa" or "santa":
    print("You're NOT Santa!")

# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation (the + operator).

title = "Code"
author = "Charles Petzold"

print("The book I am reading right now is " + title + ", by " + author) + "."

# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation (the #{} operator).

title = "Code"
author = "Charles Petzold"

print(f"The book I am reading right now is {title}, by {author}.")

# Write a program that asks the user to enter a password. If the password is "Joshua", the program responds "Shall we play a game?". For any other password, the program responds "Access denied"

password = input("Please enter a password: ")
if password == "Joshua":
    print("Shall we play a game?")
else:
    print("ACCESS DENIED")
