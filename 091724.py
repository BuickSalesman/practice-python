import random

# Write a ShoppingCart class that stores an array of items with methods to add an item, remove an item, and display all the items.


class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)

    def display_items(self):
        print(f"The items in the cart are: ")
        for item in self.items:
            print(f"- {item}")


cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Orange")
cart.display_items()
cart.remove_item("Banana")
cart.display_items()
# Write a Product class that stores the name, price, and metadata, where metadata is a hash that stores additional information about the product.


class Product:
    def __init__(self, name, price, metadata):
        self.name = name
        self.price = price
        self.metadata = metadata


product = Product("Laptop", 999, {"color": "red", "nice": "sure"})
print("Product Details:")
print(f"Name: {product.name}")
print(f"Price: ${product.price}")
print(f"Metadata: {product.metadata}")
print(f"Brand: {product.metadata['nice']}")
print(f"Color: {product.metadata['color']}")

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

    def shuffle(self):
        random.shuffle(self.songs)

    def display_playlist(self):
        print(f"Playlist: {self.name}")
        print("Songs in playlist:")
        for song in self.songs:
            print("- " + song)


playlist = Playlist("My Playlist")
playlist.add_song("Song 1")
playlist.add_song("Song 2")
playlist.add_song("Song 3")
playlist.add_song("Song 4")
playlist.display_playlist()
playlist.remove_song("Song 2")
playlist.display_playlist()
playlist.shuffle()
playlist.display_playlist()


# Write a Contact class that stores the name, age, and contact_info, where contact_info is a hash that stores any additional information about the contact.

class Contact:
    def __init__(self, name, age, contact_info):
        self.name = name
        self.age = age
        self.contact_info = contact_info


person = Contact("John Doe", 30, {
    "phone": "123-456-7890", "email": "john@example.com"})

print("Person Details:")
print(f"Name: {person.name}")
print(f"Age: {person.age}")
print(f"Contact Info: {person.contact_info}")
print(f"Phone: {person.contact_info['phone']}")
print(f"Email: {person.contact_info['email']}")
