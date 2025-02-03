# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

numbers = [5, 10, 8, 3]
sum = sum(numbers)
print(sum)

# Start with an array of strings and combine them all into a single string.
# For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

words = ["volleyball", "basketball", "badminton"]
combined_words = "".join(words)
print(combined_words)

# Start with an array of hashes and compute the sum of the prices (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

total_items_price = 0
for item in items:
    total_items_price += item["price"]

print(total_items_price)
# Start with an array of numbers and compute the the minumum number.
# For example, [5, 10, 8, 3, 9] becomes 3.

numbers = [5, 10, 8, 3, 9]
minimum_number = numbers[0]

for number in numbers:
    if number < minimum_number:
        minimum_number = number

print(minimum_number)

# Start with an array of strings and compute the total length of all the strings.
# For example, ["volleyball", "basketball", "badminton"] becomes 29.

words = ["volleyball", "basketball", "badminton"]
total_length = 0
for word in words:
    total_length += len(word)

print(total_length)

# Start with an array of hashes and find the hash with the lowest price (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

lowest_price_item = items[0]

for item in items:
    if item["price"] < lowest_price_item["price"]:
        lowest_price_item = item

print(lowest_price_item)
