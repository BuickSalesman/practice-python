# 1. Sum of even numbers using lambda
# Start with an array of numbers and compute the sum of all even numbers using a lambda function. Example: [5, 10, 8, 3] becomes 18.

numbers = [5, 10, 8, 3]
even_sum = sum(filter(lambda number: number % 2 == 0, numbers))
print(even_sum)

# 2. Filter out strings longer than 5 characters
# Start with an array of strings and use a lambda function to filter out strings longer than 5 characters. Example: ["apple", "banana", "pear"] becomes ["apple", "pear"].

fruits = ["apple", "banana", "pear"]
short_name_fruits = list(filter(lambda fruit: len(fruit) <= 5, fruits))
print(short_name_fruits)


# 3. Sort an array of hashes by price using lambda
# Sort an array of hashes by the price key using a lambda function. Example: [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes sorted by price.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

sorted_items = list(sorted(items, key=lambda item: item["price"]))
print(sorted_items)

# 4. Square all numbers in an array using lambda
# Start with an array of numbers and square each one using a lambda function. Example: [2, 3, 4] becomes [4, 9, 16].

numbers = [2, 3, 4]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)

# 5. Combine strings into a single string separated by spaces using lambda
# Start with an array of strings and combine them into a single string separated by spaces using a lambda function. Example: ["hello", "world"] becomes "hello world".

words = ["hello", "world"]
stringified_words = " ".join(map(lambda word: str(word), words))
print(stringified_words)


# 6. Find the longest string using lambda
# Start with an array of strings and use a lambda function to find the longest string. Example: ["cat", "elephant", "dog"] becomes "elephant".

animals = ["cat", "elephant", "dog"]
longest_name_animal = max(animals, key=lambda animal: len(animal))
print(longest_name_animal)


# 7. Multiply all numbers in an array using lambda (without reduce)
# Start with an array of numbers and compute the product of all numbers using a lambda function. Example: [2, 3, 4] becomes 24.

numbers = [2, 3, 4]
product = 1
def multiply(product, number): return product * number


for number in numbers:
    product = multiply(product, number)

print(product)


# 8. Find strings that start with a specific letter using lambda
# Start with an array of strings and use a lambda function to find all strings that start with a specific letter (e.g., 'a'). Example: ["apple", "banana", "avocado"] becomes ["apple", "avocado"].

fruits = ["apple", "banana", "avocado"]
a_fruits = list(filter(lambda fruit: fruit[0] == "a", fruits))
print(a_fruits)

# print(starts_with_a)
# 9. Find the number with the most digits using lambda
# Start with an array of numbers and use a lambda function to find the number with the most digits. Example: [100, 20, 3000, 4] becomes 3000.

numbers = [100, 20, 3000, 4]
most_digits = max(numbers, key=lambda number: len(str(number)))
print(most_digits)

# 10. Remove duplicates from an array using lambda
# Start with an array of numbers and use a lambda function to remove duplicates. Example: [1, 2, 2, 3, 4, 4] becomes [1, 2, 3, 4].

numbers = [1, 2, 2, 3, 4, 4]


def add_unique(
    list, number): return list if number in list else list + [number]


no_dups = []

for number in numbers:
    no_dups = add_unique(no_dups, number)

print(no_dups)
