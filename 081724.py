# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

numbers = [5, 10, 8, 3]
numbers_sum = sum(numbers)
print(numbers_sum)

# Start with an array of strings and combine them all into a single string.
# For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

sports = ["volleyball", "basketball", "badminton"]
combined_sports = "".join(sports)
print(combined_sports)


# Start with an array of hashes and compute the sum of the prices (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

items_price_sum = sum(item["price"] for item in items)
print(items_price_sum)

# Start with an array of numbers and compute the the minumum number.
# For example, [5, 10, 8, 3, 9] becomes 3.

numbers = [5, 10, 8, 3, 9]
minimum_number = min(numbers)
print(minimum_number)

# Start with an array of strings and compute the total length of all the strings.
# For example, ["volleyball", "basketball", "badminton"] becomes 29.

sports = ["volleyball", "basketball", "badminton"]
sports_length = sum(len(sport) for sport in sports)
print(sports_length)

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

# Start with an array of numbers and compute product of all the numbers.
# For example, [5, 10, 8, 3] becomes 1200.

numbers = [5, 10, 8, 3]
numbers_product = 1
for number in numbers:
    numbers_product *= number

print(numbers_product)

# Start with an array of strings and combine them all into a single string, separated by dashes.
# For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

sports = ["volleyball", "basketball", "badminton"]
dash_joined_sports = "-" + "-".join(sports) + "-"
print(dash_joined_sports)

# Start with an array of hashes and find the hash with the shortest name (from the :name key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

shortest_name_item = items[0]

for item in items:
    if len(item["name"]) < len(shortest_name_item["name"]):
        shortest_name_item = item

print(shortest_name_item)

# Start with an array of numbers and compute the maximum number.
# For example, [5, 10, 8, 3] becomes 10.

numbers = [5, 10, 8, 3]
maximum_number = max(numbers)
print(maximum_number)
