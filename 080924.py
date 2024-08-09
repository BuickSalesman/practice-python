# Write a ShoppingCart class that stores an array of items with methods to add an item, remove an item, and display all the items.


import random


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_cart(self):
        print("The items in the cart are:")
        for item in self.items:
            print(f"- {item}")


cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Orange")
cart.add_item("Doritos")
cart.display_cart()
cart.remove_item("Orange")
cart.display_cart()

# Write a Product class that stores the name, price, and metadata, where metadata is a hash that stores additional information about the product.


class Product:
    def __init__(self, name, price, metadata):
        self.name = name
        self.price = price
        self.metadata = metadata


product = Product("iPhone", 499, {"make": "Apple", "color": "silver"})
print(product.name)
print(product.price)
print(product.metadata["make"])
print(product.metadata["color"])

# Write a Playlist class that stores a name and an array of songs with methods to add a song, remove a song, shuffle the songs into a random order, and display all the songs.


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def shuffle_playlist(self):
        random.shuffle(self.songs)

    def display_songs(self):
        print(f"Playlist: {self.name}")
        print("Songs in playlist are:")
        for song in self.songs:
            print(f"- {song}")


playlist = Playlist("Cool Pants")
playlist.add_song("Mr BrightSide")
playlist.add_song("CBAT")
playlist.add_song("Ghosts N Stuff")
playlist.add_song("I Wish I Knew How It Would Feel To Be Free")
playlist.add_song("A Tune For Jack")
playlist.display_songs()
playlist.shuffle_playlist()
playlist.display_songs()
playlist.remove_song("Ghosts N Stuff")
playlist.shuffle_playlist()
playlist.display_songs()
