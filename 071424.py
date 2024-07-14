# Write a Song class with attributes and reader/writer methods for name, artist, and duration. Then write a method that prints the name, artist, and duration in a single sentence.

class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration

    def print_info(self):
        print(
            f"The song {self.name}, by {self.artist}, has a duration on {self.duration}")


song = Song("Tomorrow Comes Today", "Gorillaz", "3:13")
song.print_info()

# Write a Rectangle class with attributes and reader/writer methods for width and height. Then write a method that returns the area of the rectangle.


class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        return self.height * self.width


rectangle = Rectangle(6, 7)
print(rectangle.get_area())

# Write a Person class with attributes and reader/writer methods for name and age. Then write a method that returns the person's name in all capital letters.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def capitalize_name(self):
        return self.name.upper()


person = Person("Kelsey", 26)
print(person.capitalize_name())


# Write an Account class with attributes and reader/writer methods for name and balance. Then write a method that prints a warning if the balance is below $100.

class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def low_balance(self):
        if self.balance < 100:
            print("WARNING U R BROKE")


account = Account("Checking", 5)
account.low_balance()

# Write a Movie class with attributes and reader/writer methods for title, director, and year. Then write a method that prints out the attributes in a single sentence.


class Movie:
    def __init__(self, title, director, year):
        self.title = title
        self.director = director
        self.year = year

    def print_info(self):
        print(
            f"The movie {self.title}, directed by {self.director}, came out in {self.year}."
        )


movie = Movie("Whatever: The Movie", "Brad Schmitt", 1888)
movie.print_info()
# Write a Car class with attributes and reader/writer methods for make, model, year, and color. Then write a method that returns the make and model as a single sentence in all lowercase letters.


class Car:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def lower_case_info(self):
        print(f"{self.make.lower()} {self.model.lower()} ")


car = Car("KIA", "CRV", 1934, "red")
car.lower_case_info()

# Write a Point class with attributes and reader/writer methods for x, y, and z coordinates. Then write a method that returns true if all 3 numbers are positive, otherwise it returns false.


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def check_positive(self):
        return self.x > 0 and self.y > 0 and self.z > 0


point = Point(8, 9, -2)
print(point.check_positive())
