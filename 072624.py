# Write a Song class with attributes and reader/writer methods for name, artist, and duration. Then write a method that prints the name, artist, and duration in a single sentence.

class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

    def song_info(self):
        print(
            f"The song {self.name} by {self.artist}, has a duration of {self.duration}."
        )


song = Song("Tomorrow Comes Today", "Gorillaz", "3:13")
song.song_info()

# Write a Rectangle class with attributes and reader/writer methods for width and height. Then write a method that returns the area of the rectangle.


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        area = self.height * self.width
        return area


rectangle = Rectangle(6, 8)
print(rectangle.get_area())

# Write a Person class with attributes and reader/writer methods for name and age. Then write a method that returns the person's name in all capital letters.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def name_in_capitals(self):
        return self.name.upper()


person = Person("Kelsey", 26)
print(person.name_in_capitals())

# Write a Coordinate class with attributes and reader/writer methods for latitude and longitude. Then write a method that prints out the latitude and longitude in a single sentence.


class Coordinate:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def get_lon_lan(self):
        print(
            f"The coordinate has a latitude of {self.lat}, and a longitude of {self.lon}."
        )


coordinate = Coordinate(04.789243, -18.235242)
coordinate.get_lon_lan()

# Write an Account class with attributes and reader/writer methods for name and balance. Then write a method that prints a warning if the balance is below $100.


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def low_balance_warning(self):
        if self.balance < 100:
            print(f"u suck u broke u only got {self.balance} dolla in dere")


account = Account("Checking", 5)
account.low_balance_warning()


# Write a Movie class with attributes and reader/writer methods for title, director, and year. Then write a method that prints out the attributes in a single sentence.

class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def get_movie_info(self):
        print(
            f"The movie {self.title}, directed by {self.director}, was released in {self.year}."
        )


movie = Movie("It's Such A Beautiful Day", "Don Hertzfeldt", "2012")
movie.get_movie_info()


# Write a Point class with attributes and reader/writer methods for x, y, and z coordinates. Then write a method that returns true if all 3 numbers are positive, otherwise it returns false.

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_positive(self):
        return self.x > 0 and self.y > 0 and self.z > 0


point = Point(-2, 3, 4)
print(point.is_positive())

# Write a Book class with attributes and reader/writer methods for title, author, and year. Then write a method that returns "Classic" if the book is older than 2000, otherwise it returns "Modern".


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def is_classic(self):
        if self.year < 2000:
            return "Classic"
        else:
            return "Modern"


book = Book("Code", "Charles Petzold", 1999)
print(book.is_classic())

# Write a Plant class with attributes and reader/writer methods for name, size, and price. Then write a method that prints out the attributes in a single sentence.


class Plant:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def plant_info(self):
        print(
            f"My new plant, {self.name}, is the size of {self.size}, and only cost me {self.price} dollars!"
        )


plant = Plant("Acer Rubrum", "a big ol tree", 500)
plant.plant_info()
