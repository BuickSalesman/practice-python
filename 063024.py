# Write a Song class with attributes for name, artist, and duration.


class Song:
    def __init__(self, name, artist, duration):
        self.name = name
        self.artist = artist
        self.duration = duration


song = Song("Tomorrow Comes Today", "Gorillaz", "3:13")
print(f"{song.name}, {song.artist}, {song.duration}")


# Write a Rectangle class with attributes for width and height.


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height


rectangle = Rectangle(4, 5)
print(f"{rectangle.width, rectangle.height}")


# Write a Person class with attributes for name and age.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person = Person("Kate", 26)
print(f"{person.name, person.age}")


# Write a Location class with attributes for latitude and longitude.


class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


location = Location(3.4564, -17.6790)
print(f"{location.latitude, location.longitude}")


# Write an Account class with attributes for name and balance.


class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance


account = Account("Chcecking", 500)
print(f"Your {account.name} account has a balance of ${account.balance}")
