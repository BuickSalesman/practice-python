# Make a hash to store a person's first name, last name, and email address. Then print each attribute on separate lines.


person = {
    "first_name": "Kelsey",
    "last_name": "Kavanagh",
    "email": "1234@gmail.com"
}

print(person["first_name"])
print(person["last_name"])
print(person["email"])

# Make an array of hashes to store the first name and last name for 3 different people. Then print out the first person's info.

names = [
    {"first_name": "Kelsey", "last_name": "Kavanagh"},
    {"first_name": "Adam", "last_name": "O'Donnell"},
    {"first_name": "Jacob", "last_name": "Baker"}
]

print(names[0])

# Make a hash to store prices for 3 different menu items. Then add a new menu item and price and print the hash to see the result.

menu = {"burger": 10, "wings": 8, "fries": 4, }
menu["fried pickles"] = 6

print(menu)

# Make a hash to store a book's title, author, number of pages, and language. Then print each attribute on separate lines.

book = {
    "title": "CODE",
    "author": "Charles Petzold",
    "pages": 700,
    "language": "English"
}

print(book["title"])
print(book["author"])
print(book["pages"])
print(book["language"])


# Make an array of hashes to store the title and author for 3 different books. Then print out the third book's author.

books = [
    {"title": "CODE", "author": "Charles Petzold"},
    {"title": "99 Bottle of OOP", "author": "Sandi Metz"},
    {"title": "The Non-Designer's Design Book", "author": "Robin Williams"}
]

print(books[2]["author"])

# Make a hash to store 3 different states and their captitals. Then add a new state and capital and print the hash to see the
# result.

capitals = {
    "oregon": "salem",
    "california": "sacremento",
    "missouri": "jefferson city"
}

capitals["georgia"] = "atlanta"

print(capitals)

# Make a hash to store a laptop's brand, model, and year. Then print each attribute on separate lines.

laptop = {"brand": "apple", "model": "m1", "year": "2023"}
print(laptop["model"])
print(laptop["brand"])
print(laptop["year"])

# Make an array of hashes to store the brand and model for 3 different laptops. Then print out the second laptop's model.

laptops = [
    {"brand": "best brand", "model": "best laptop"},
    {"brand": "worst brand", "model": "worst model"},
    {"brand": "ok brand", "model": "ok model"}
]

print(laptops[1]["model"])

# Make a hash to store definitions for 2 different words. Then add a new word and definition and print the hash to see the result.

definitions = {
    "sycophant": "a person who acts obsequiously toward someone important in order to gain advantage.",
    "obsequious": "obedient or attentive to an excessive or servile degree.",
}

definitions["servile"] = "submissive or fawning in attitude or behavior."

print(definitions)

# Make a hash to store a shirt's brand, color, and size. Then print each attribute on separate lines.

shirt = {"brand": "brand", "color": "color", "size": "size"}

print(shirt["brand"])
print(shirt["color"])
print(shirt["size"])
