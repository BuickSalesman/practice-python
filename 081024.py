# Write a program that uses variables to store a first and last name, then prints the full name in one line using string concatenation(the + operator).

first_name = "Dennis"
last_name = "Vanterpool"
print(first_name + " " + last_name)


# Write a program that uses variables to store a first and last name, then prints the full name in one line using string interpolation(the  # {} operator).

first_name = "Dennis"
last_name = "Vanterpool"
print(f"{first_name} {last_name}")


# Write a program that asks the user to input a word. If the word is "marco", print "polo".
word = input("Please enter a word: ")
if word == "marco":
    print("polo")


# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string concatenation(the + operator).
color1 = "red"
color2 = "blue"
color3 = "green"

print(
    "The colors I have stored in variables are " +
    color1 + ", " + color2 + ", and " + color3 + "."
)


# Write a program that uses variables to store three different colors, then prints out a sentence using the colors with string interpolation(the  # {} operator).
color1 = "red"
color2 = "blue"
color3 = "green"

print(
    f"The colors I have stored in variables are {color1}, {color2}, and {color3}."
)


# Write a program that asks the user to enter a name. If the name is not "Santa", print "You're not Santa."

name = input("Please enter your name: ")
if name != "Santa" and name != "santa":
    print("You're not Santa!")


# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string concatenation(the + operator).

title = "CODE"
author = "Charles Petzold"

print("The book is called " + title + ", by " + author + ".")


# Write a program that uses variables to store a book's title and author, then prints out a sentence using that information with string interpolation(the  # {} operator).

title = "CODE"
author = "Charles Petzold"

print(f"The book is called {title}, by {author}.")
