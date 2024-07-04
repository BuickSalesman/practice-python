# Start with an array of numbers and create a new array with only the numbers less than 10.
# For example, [8, 23, 0, 44, 1980, 3] becomes [8, 0, 3].

numbers = [8, 24, 0, 33, 1980, 3, 1776, 7, 4]
numbers_less_than_ten = [number for number in numbers if number < 10]
print(numbers_less_than_ten)


# Start with an array of strings and create a new array with only the strings that don't start with the letter "b".
# For example, ["big", "little", "good", "bad"] becomes ["little", "good"].

strings = ["big", "little", "good", "bad"]
not_b_strings = [s for s in strings if not s.startswith("b")]
print(not_b_strings)


# Start with an array of hashes and create a new array with only the hashes with prices less than 10 (from the: price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes[{name: "pencil", price: 1}, {name: "book", price: 4}].

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

cheap_items = [item for item in items if item["price"] < 10]
print(cheap_items)


# Start with an array of numbers and create a new array with only the odd numbers.
# For example, [2, 4, 5, 1, 8, 9, 7] becomes [5, 1, 9, 7].

numbers = [2, 4, 5, 1, 8, 9, 7]
odd_numbers = [num for num in numbers if num % 2 != 0]
print(odd_numbers)


# Start with an array of numbers and compute the sum of all the numbers.
# For example, [5, 10, 8, 3] becomes 26.

numbers = [5, 10, 8, 3]
total_sum = sum(numbers)
print(total_sum)

# Start with an array of strings and combine them all into a single string.
# For example, ["volleyball", "basketball", "badminton"] becomes "volleyballbasketballbadminton".

strings = ["volleyball", "basketball", "badminton"]
combined_strings = "".join(strings)
print(combined_strings)


# Start with an array of hashes and compute the sum of the prices (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes 105.


items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

total_price = sum(item["price"] for item in items)
print(total_price)


# Start with an array of numbers and compute the the minumum number.
# For example, [5, 10, 8, 3, 9] becomes 3.

numbers = [5, 10, 8, 3, 9]
smallest_number = numbers[0]

for num in numbers:
    if num < smallest_number:
        smallest_number = num

print(smallest_number)


# Start with an array of strings and compute the total length of all the strings.
# For example, ["volleyball", "basketball", "badminton"] becomes 29

strings = ["volleyball", "basketball", "badminton"]
length_of_strings = sum(len(s) for s in strings)
print(length_of_strings)


# Start with an array of hashes and find the hash with the lowest price (from the :price key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "pencil", price: 1}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

smallest_price = items[0]["price"]
cheapest_item = items[0]


for item in items:
    if item["price"] < smallest_price:
        smallest_price = item["price"]
        cheapest_item = item

print(cheapest_item)


# Start with an array of numbers and compute product of all the numbers.
# For example, [5, 10, 8, 3] becomes 1200.

numbers = [5, 10, 8, 3]

product = 1
for num in numbers:
    product *= num

print(product)


# Start with an array of strings and combine them all into a single string, separated by dashes.
# For example, ["volleyball", "basketball", "badminton"] becomes "-volleyball-basketball-badminton-".

strings = ["volleyball", "basketball", "badminton"]

combined_strings = f"-{'-'.join(strings)}-"

print(combined_strings)


# Start with an array of hashes and find the hash with the shortest name (from the :name key).
# For example, [{name: "chair", price: 100}, {name: "pencil", price: 1}, {name: "book", price: 4}] becomes {name: "book", price: 4}.

items = [
    {"name": "chair", "price": 100},
    {"name": "pencil", "price": 1},
    {"name": "book", "price": 4}
]

shortest_name = len(items[0]["name"])
shortest_name_item = items[0]

for item in items:
    if len(item["name"]) < shortest_name:
        shortest_name = len(item["name"])
        shortest_name_item = item

print(shortest_name_item)


# Start with an array of numbers and compute the maximum number.
# For example, [5, 10, 8, 3] becomes 10.

numbers = [1, 4, 656, 3, 6789, 10]
maximum_number = max(numbers)
print(maximum_number)
