# Write a program that stores a customer's age and a movie's time in two separate variables. Then calculate the price of a movie ticket based on the following conditions:

# If the age is 12 years old or younger, the ticket price is $5.
# If the age is between 13 and 59 years old and the movie is before 6 PM, the ticket price is $7. After 6 PM, the ticket price is $10.
# If the customer is 60 years old or older, the ticket price is $7.

age = 70
time = 18

ticket_price = None

if age <= 12:
    ticket_price = 5
elif age >= 13 and age <= 59:
    if time < 18:
        ticket_price = 7
    else:
        ticket_price = 10
else:
    ticket_price = 7

print(ticket_price)

# Write a program to store the type of book (regular, reference, or special collection) and the number of days its overdue. Then calculate the fine amount based on the following conditions:

# If the book is a regular book and overdue by up to 7 days, the fine is $1 per day.
# If the book is a regular book and overdue by more than 7 days, the fine is $2 per day.
# If the book is a reference book, there is no fine, regardless of the number of days overdue.
# If the book is a special collection book, the fine is $5 per day, regardless of the number of days overdue.

book_type = "reference"
days_overdue = 60

fine = None

if book_type == "regular":
    if days_overdue <= 7:
        fine = days_overdue
    else:
        fine = days_overdue * 2
elif book_type == "reference":
    fine = 0
elif book_type == "special collection":
    fine = days_overdue * 5

print(fine)

# Write a program that stores a person's order value and membership level (regular or premium). Then calculate a discount amount based on the following conditions:

# If the total order value is less than $50, there is no discount.
# If the total order value is between $50 and $100, the discount is 5% for regular customers and 10% for premium customers.
# If the total order value is greater than $100, the discount is 10% for regular customers and 15% for premium customers.

order_value = 176
membership_level = "premium"

discount = None


if order_value < 50:
    discount = 0
elif order_value >= 50 and order_value <= 100:
    if membership_level == "regular":
        discount = order_value * .05
    elif membership_level == "premium":
        discount = order_value * .10
elif order_value > 100:
    if membership_level == "regular":
        discount = order_value * .10
    elif membership_level == "premium":
        discount = order_value * .15

total_with_discount = order_value - discount
print(total_with_discount)

# Write a Ruby program that stores the weight of a package and the destination (domestic or international). Then calculate the shipping fee based on the following conditions:

# If the destination is domestic:
# If the weight is less than or equal to 1 kg, the shipping fee is $5.
# If the weight is greater than 1 kg, the shipping fee is $10.
# If the destination is an international shipment:
# If the weight is less than or equal to 1 kg, the shipping fee is $15.
# If the weight is greater than 1 kg, the shipping fee is $25.

weight = 14
destination = "international"

shipping_fee = None

if destination == "domestic":
    if weight <= 1:
        shipping_fee = 5
    else:
        shipping_fee = 10
elif destination == "international":
    if weight <= 1:
        shipping_fee = 15
    else:
        shipping_fee = 25


print(shipping_fee)


# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes [3, 6, 9].

numbers = [1, 2, 3]
new_numbers = [number * 3 for number in numbers]
print(new_numbers)


# Start with an array of strings and create a new array with each string upcased.
# For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

words = ["hello", "goobye"]
big_words = [word.upper() for word in words]
print(big_words)


# Start with an array of hashes and create a new array of string values from each hash's :name key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
names = [person["name"] for person in people]
print(names)


# Start with an array of numbers and create a new array with each number plus 7.
# For example, [1, 2, 3] becomes [8, 9, 10].

numbers = [1, 2, 3]
numbers_plus_7 = [number + 7 for number in numbers]
print(numbers_plus_7)


# Start with an array of strings and create a new array with each string's length.
# For example, ["hello", "goodbye"] becomes [5, 7].

words = ["hello", "goodbye"]
word_lengths = [len(word) for word in words]
print(word_lengths)


# Start with an array of hashes and create a new array of number values from each hash's :age key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [27, 16].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages = [person["age"] for person in people]
print(ages)


# Start with an array of numbers and create a new array with each number divided by 2.
# For example, [1, 2, 3] becomes [0.5, 1.0, 1.5].

numbers = [1, 2, 3]
divided_numbers = [number / 2 for number in numbers]
print(divided_numbers)


# Start with an array of strings and create a new array with each string's first letter only.
# For example, ["hello", "goodbye"] becomes ["h", "g"].

words = ["hello", "goodbye"]
first_letters = [word[0] for word in words]
print(first_letters)


# Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages_times_two = [person["age"] * 2 for person in people]
print(ages_times_two)


# Start with an array of numbers and create a new array with each number converted into a string.
# For example, [1, 2, 3] becomes ["1", "2", "3"].

numbers = [1, 2, 3]
stringy_numbers = [str(number) for number in numbers]
print(stringy_numbers)
