# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

numbers = [5, 10, 8, 3]
sum_of_numbers = sum(numbers)
print(sum_of_numbers)

# Start with an array of strings and combine them all into a single string.
# For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

strings = ["volleyball", "basketball", "badminton"]
combined_strings = "".join(string for string in strings)
print(combined_strings)


# Start with an array of hashes and compute the sum of the prices(from the: price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

combined_prices = sum(item["price"] for item in items)
print(combined_prices)

# Start with an array of numbers and compute the the minimum number.
# For example, [5, 10, 8, 3, 9] becomes 3.

numbers = [5, 10, 8, 3, 9]
minimum_number = min(numbers)
print(minimum_number)


# Start with an array of strings and compute the total length of all the strings.
# For example, ["volleyball", "basketball", "badminton"] becomes 29.

sports = ["volleyball", "basketball", "badminton"]
length = sum(len(string) for string in strings)
print(length)


# Start with an array of hashes and find the hash with the lowest price(from the: price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

lowest_price_item = min(items, key=lambda item: item["price"])
print(lowest_price_item)

# Start with an array of numbers and compute product of all the numbers.
# For example, [5, 10, 8, 3] becomes 1200.

numbers = [5, 10, 8, 3]
product = 1
for number in numbers:
    product = product * number
print(product)


# Start with an array of strings and combine them all into a single string, separated by dashes.
# For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

sports = ["volleyball", "basketball", "badminton"]
conjoined_sports = "-" + "-".join(sport for sport in sports) + "-"
print(conjoined_sports)

# Start with an array of hashes and find the hash with the shortest name(from the: name key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

shortest_name_item = min(items, key=lambda item: item["name"])
print(shortest_name_item)

# Start with an array of numbers and compute the maximum number.
# For example, [5, 10, 8, 3] becomes 10.

numbers = [5, 10, 8, 3]
maximum = max(numbers)
print(maximum)

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

sorted_items = sorted(items, key=lambda item: item["price"])
print(sorted_items)

# 4. Square all numbers in an array using lambda
# Start with an array of numbers and square each one using a lambda function. Example: [2, 3, 4] becomes [4, 9, 16].

numbers = [2, 3, 4]
squared_numbers = list(map(lambda number: number ** 2, numbers))
print(squared_numbers)


# 5. Combine strings into a single string separated by spaces using lambda
# Start with an array of strings and combine them into a single string separated by spaces using a lambda function. Example: ["hello", "world"] becomes "hello world".

words = ["hello", "world"]
words_string = " ".join(map(lambda word: word, words))
print(words_string)


# 6. Find the longest string using lambda
# Start with an array of strings and use a lambda function to find the longest string. Example: ["cat", "elephant", "dog"] becomes "elephant".

animals = ["cat", "elephant", "dog"]
longest_name_animal = max(animals, key=lambda animal: len(animal))
print(longest_name_animal)


# 7. Multiply all numbers in an array using lambda (without reduce)
# Start with an array of numbers and compute the product of all numbers using a lambda function. Example: [2, 3, 4] becomes 24.

numbers = [2, 3, 4]
product = 1
# multiple = lambda x, y: x * y
def multiply(x, y): return x * y


for number in numbers:
    product = multiply(product, number)

print(product)

# 8. Find strings that start with a specific letter using lambda
# Start with an array of strings and use a lambda function to find all strings that start with a specific letter (e.g., 'a'). Example: ["apple", "banana", "avocado"] becomes ["apple", "avocado"].

fruits = ["apple", "banana", "avocado"]
a_fruits = list(filter(lambda fruit: fruit[0] == "a", fruits))
print(a_fruits)


# 9. Find the number with the most digits using lambda
# Start with an array of numbers and use a lambda function to find the number with the most digits. Example: [100, 20, 3000, 4] becomes 3000.

numbers = [100, 20, 3000, 4]
most_digits_number = max(numbers, key=lambda number: len(str(number)))
print(most_digits_number)

# 10. Remove duplicates from an array using lambda
# Start with an array of numbers and use a lambda function to remove duplicates. Example: [1, 2, 2, 3, 4, 4] becomes [1, 2, 3, 4].

numbers = [1, 2, 2, 3, 4, 4]
# add_unique = lambda list, num: list if num in list else list + [num]
def add_unique(list, num): return list if num in list else list + [num]


no_duplicates_numbers = []
for number in numbers:
    no_duplicates_numbers = add_unique(no_duplicates_numbers, number)

print(no_duplicates_numbers)
