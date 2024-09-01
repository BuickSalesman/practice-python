# Write a program that stores a customer's age and a movie's time in two separate variables. Then calculate the price of a movie ticket based on the following conditions:

# If the age is 12 years old or younger, the ticket price is $5.
# If the age is between 13 and 59 years old and the movie is before 6 PM, the ticket price is $7. After 6 PM, the ticket price is $10.
# If the customer is 60 years old or older, the ticket price is $7.

age = 14
showtime = 19
price = None

if age <= 12:
    price = 5
elif age >= 13 and age <= 59:
    if showtime < 16:
        price = 7
    elif showtime >= 16:
        price = 10
elif age >= 60:
    price = 7

print(price)

# Write a program to store the type of book (regular, reference, or special collection) and the number of days its overdue. Then calculate the fine amount based on the following conditions:

# If the book is a regular book and overdue by up to 7 days, the fine is $1 per day.
# If the book is a regular book and overdue by more than 7 days, the fine is $2 per day.
# If the book is a reference book, there is no fine, regardless of the number of days overdue.
# If the book is a special collection book, the fine is $5 per day, regardless of the number of days overdue.

type = "regular"
days_overdue = 12
fine = None

if type == "regular":
    if days_overdue <= 7:
        fine = days_overdue
    elif days_overdue > 7:
        fine = days_overdue * 2
elif type == "references":
    fine = 0
elif type == "special collection":
    fine = days_overdue * 5

print(fine)

# Write a program that stores a person's order value and membership level (regular or premium). Then calculate a discount amount based on the following conditions:

# If the total order value is less than $50, there is no discount.
# If the total order value is between $50 and $100, the discount is 5% for regular customers and 10% for premium customers.
# If the total order value is greater than $100, the discount is 10% for regular customers and 15% for premium customers.

order_amount = 74
membership = "regular"
discount = None

if order_amount < 50:
    discount = 0
elif order_amount >= 50 and order_amount <= 100:
    if membership == "regular":
        discount = order_amount * .05
    elif membership == "premium":
        discount = order_amount * .10
elif order_amount > 100:
    if membership == "regular":
        discount = order_amount * .10
    elif membership == "premium":
        discount = order_amount * .15

print(order_amount - discount)
