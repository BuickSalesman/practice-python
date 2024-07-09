# Make a hash to store a person's first name, last name, and email address. Then print each attribute on separate lines.

person = {
    "first_name": "Kelsey",
    "last_name": "Kavanagh",
    "email": "kelsey123@gmail.com"
}

print(person["first_name"])
print(person["last_name"])
print(person["email"])

# Make an array of hashes to store the first name and last name for 3 different people. Then print out the first person's info.

people = [
    {"first_name": "Adam", "last_name": "O'Donnell"},
    {"first_name": "Kelsey", "last_name": "Kavanagh"},
    {"first_name": "Jacob", "last_name": "Baker"}
]

print(people[0])

# Make a hash to store prices for 3 different menu items. Then add a new menu item and price and print the hash to see the result.

menu = {"burger": 5, "fries": 2, "salad": 3}
menu["smoothie"] = 3
print(menu)


# Make a hash to store a book's title, author, number of pages, and language. Then print each attribute on separate lines.

book = {
    "title": "Code",
    "author": "Charles Petzold",
    "number_of_pages": 700,
    "language": "English"
}

print(book["title"])
print(book["author"])
print(book["number_of_pages"])
print(book["language"])


# Make an array of hashes to store the title and author for 3 different books. Then print out the third book's author.

books = [
    {"title": "Code", "author": "Charles Petzold"},
    {"title": "A Series of Unfortunate Events", "author": "Lemony Snicket"},
    {"title": "Lord of the Rings", "author": "John Railroad Tolkien"}
]

print(books[2]["author"])

# Make a hash to store 3 different states and their captitals. Then add a new state and capital and print the hash to see the

capitals = {
    "Missouri": "Jefferson City",
    "Georgia": "Atlanta",
    "California": "Sacremento"
}

capitals["Oregon"] = "Salem"
print(capitals)


# Make a hash to store a laptop's brand, model, and year. Then print each attribute on separate lines.

laptop = {"brand": "Apple", "model": "M1", "year": 2024}
print(laptop["brand"])
print(laptop["model"])
print(laptop["year"])
