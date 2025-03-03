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

people = [
    {"first_name": "adam", "last_name": "odonnell"},
    {"first_name": "kelsey", "last_name": "kavanagh"},
    {"first_name": "jacob", "last_name": "baker"}
]

print(people[0])

# Make a hash to store prices for 3 different menu items. Then add a new menu item and price and print the hash to see the result.

menu = {"burger": 5, "fries": 2, "juice": 3}
menu["salad"] = 3

print(menu)

# Make a hash to store a book's title, author, number of pages, and language. Then print each attribute on separate lines.

book = {
    "Title": "Code",
    "Author": "Charles Petzold",
    "Pages": 700,
    "Language": "English"
}

print(book["Title"])
print(book["Author"])
print(book["Pages"])
print(book["Language"])

# Make an array of hashes to store the title and author for 3 different books. Then print out the third book's author.

books = [
    {
        "Title": "Code",
        "Author": "Charles Petzold"
    },
    {
        "Title": "Plant Systematics",
        "Author": "Michael G. Simpson"
    },
    {
        "Title": "The Story Of Ferdinand",
        "Author": "Munro Leaf"
    }
]

print(books[2]["Author"])

# Make a hash to store 3 different states and their captitals. Then add a new state and capital and print the hash to see the result

capitals = {
    "Missouri": "Jefferson City",
    "Georgia": "Atlanta",
    "Oregon": "Salem"
}

capitals["Rhode Island"] = "Providence"

print(capitals)

# Make a hash to store a laptop's brand, model, and year. Then print each attribute on separate lines.

laptop = {"brand": "Apple", "model": "M1", "year": "2023"}

print(laptop["brand"])
print(laptop["model"])
print(laptop["year"])

# Make an array of hashes to store the brand and model for 3 different laptops. Then print out the second laptop's model.

laptops = [
    {"brand": "Apple", "model": "M1"},
    {"brand": "HP", "model": "SuperLap"},
    {"brand": "Acer", "model": "Rubrum"}
]

print(laptops[1]["model"])
