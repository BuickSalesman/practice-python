# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation (the + operator).

first_name = "Peter"
last_name = "Jang"
print(first_name + " " + last_name)

# Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation (the #{} operator).

first_name = "Jeter"
last_name = "Pang"
print(f"{first_name} {last_name}")

# Write a program that asks the user to input a word. If the word is "marco", print "polo".

word = input("Enter a word: ")
if word == "marco":
    print("polo")

# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation (the + operator).

color1 = "red"
color2 = "blue"
color3 = "green"

print("My favorite colors are " + color1 +
      ", " + color2 + ", and " + color3 + ".")


# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation (the #{} operator).

print(f"My favorite colors are {color1}, {color2}, and {color3}.")

# Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."

name = input("Who are you? ")
if name != "Santa":
    print("You're not Santa.")

# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation (the + operator).

title = "Code"
author = "Charles Petzold"

print("The book I am reading is " + title + ", by " + author + ".")

# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation (the #{} operator).

print(f"The book I am reading is {title}, by {author}.")
