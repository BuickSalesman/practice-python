# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

numbers = [5, 10, 8, 3]
print(sum(numbers))

# Start with an array of strings and combine them all into a single string.
# For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

sports = ["volleyball", "basketball", "badminton"]
print("".join(sports))

# Start with an array of hashes and compute the sum of the prices(from the: price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

print(sum(item["price"] for item in items))


# Start with an array of numbers and compute the the minumum number.
# For example, [5, 10, 8, 3, 9] becomes 3.

numbers = [5, 10, 8, 3, 9]
print(min(numbers))

# Start with an array of strings and compute the total length of all the strings.
# For example, ["volleyball", "basketball", "badminton"] becomes 29.

sports_2 = ["volleyball", "basketball", "badminton"]
print(sum(len(sport) for sport in sports))

# Start with an array of hashes and find the hash with the lowest price(from the: price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

lowest_price_dictionary = items[0]

for item in items:
    if item["price"] < lowest_price_dictionary["price"]:
        lowest_price_dictionary = item

print(lowest_price_dictionary)

# Start with an array of numbers and compute product of all the numbers.
# For example, [5, 10, 8, 3] becomes 1200.

numbers = [5, 10, 8, 3]
sum = 1
for number in numbers:
    sum *= number

print(sum)

# Start with an array of strings and combine them all into a single string, separated by dashes.
# For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

sports_3 = ["volleyball", "basketball", "badminton", "hockey"]
sports_string = "-" + "-".join(sports_3) + "-"
print(sports_string)

# Start with an array of hashes and find the hash with the shortest name(from the: name key).
# # For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

shortest_name_item = items[0]

for item in items:
    if item["name"] < shortest_name_item["name"]:
        shortest_name_item = item

print(shortest_name_item)

# Start with an array of numbers and compute the maximum number.
# For example, [5, 10, 8, 3] becomes 10.

numbers = [5, 10, 8, 3]
print(max(numbers))
