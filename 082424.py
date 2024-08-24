# Make a hash to store a person's first name, last name, and email address. Then print each attribute on separate lines.

person = {
    "first_name": "Jacob",
    "last_name": "Baker",
    "email": "JacobBaker@gmail.com"
}

print(person["first_name"])
print(person["last_name"])
print(person["email"])

# Make an array of hashes to store the first name and last name for 3 different people. Then print out the first person's info.

people = [
    {"first_name": "Jacob", "last_name": "Baker"},
    {"first_name": "Kelsey", "last_name": "Kavanagh"},
    {"first_name": "Jeffrey", "last_name": "Baker"}
]

print(people[0])

# Make a hash to store prices for 3 different menu items. Then add a new menu item and price and print the hash to see the result.

menu = {"burger": 5, "fries": 3, "saldad": 4}
menu["tacos"] = 4
print(menu)

# Make a hash to store a book's title, author, number of pages, and language. Then print each attribute on separate lines.

book = {
    "title": "Jonathan Livingston Seagull",
    "author": "Richard Bach",
    "language": "english"
}
print(book["title"])
print(book["author"])
print(book["language"])

# Make an array of hashes to store the title and author for 3 different books. Then print out the third book's author.

books = [
    {"title": "Jonathan Livingston Seagull", "author": "Richard Bach"},
    {"title": "CODE", "author": "Charles Petzold"},
    {"title": "The Non-Designers Design Book", "author": "Robin Williams"}
]
print(books[2]["author"])

# Make a hash to store 3 different states and their capitals. Then add a new state and capital and print the hash to see the# result.

capitals = {
    "Alaska": "Juno",
    "Nevada": "Carson Ciry",
    "South Carolina": "Columbia"
}

capitals["California"] = "Sacremento"
print(capitals)

# Make a hash to store a laptop's brand, model, and year. Then print each attribute on separate lines.

laptop = {"make": "Apple", "model": "M1", "year": "2022"}
print(laptop["make"])
print(laptop["model"])
print(laptop["year"])

# Make an array of hashes to store the brand and model for 3 different laptops. Then print out the second laptop's model.

laptops = [
    {"brand": "Apple", "model": "M1"},
    {"brand": "ROG", "model": "Zephrys"},
    {"brand": "HP", "model": "HP1"},
]

print(laptops[1]["model"])

# Make a hash to store definitions for 2 different words. Then add a new word and definition and print the hash to see the result.

definitions = {"poopoo": "from a butt", "peepee": "from not from a butt"}
definitions["antidisestablishmentarianism"] = "opposition to the disestablishment of the Church of England."

print(definitions)

# Make a hash to store a shirt's brand, color, and size. Then print each attribute on separate lines.

shirt = {"brand": "H&M", "color": "green", "size": "XL"}
print(shirt["brand"])
print(shirt["color"])
print(shirt["size"])
