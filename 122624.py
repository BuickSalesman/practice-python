# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes[3, 6, 9].


numbers = [1, 2, 3]
multiplied_numbers = [num * 3 for num in numbers]
print(multiplied_numbers)


# Start with an array of strings and create a new array with each string upcased.
# For example, ["hello", "goodbye"] becomes ["HELLO", "GOODBYE"].

greetings = ["hello", "goodday"]
uppercase_greetings = [greeting.upper() for greeting in greetings]
print(uppercase_greetings)


# Start with an array of hashes and create a new array of string values from each hash's :name key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes ["Alice", "Blane"].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
names = [person["name"] for person in people]
print(names)


# Start with an array of numbers and create a new array with each number plus 7.
# For example, [1, 2, 3] becomes [8, 9, 10].

numbers = [1, 2, 3]
numbers_plus_seven = [number + 7 for number in numbers]
print(numbers_plus_seven)


# Start with an array of strings and create a new array with each string's length.
# For example, ["hello", "goodbye"] becomes [5, 7].

strings = ["hello", "goodbye"]
string_lengths = [len(string) for string in strings]
print(string_lengths)


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

strings = ["hello", "goodbye"]
first_letter_of_strings = [string[0] for string in strings]
print(first_letter_of_strings)


# Start with an array of hashes and create a new array of number values from each hash's :age key times 2.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes [54, 32].


people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages_times_two = [person["age"] * 2 for person in people]
print(ages_times_two)


# Start with an array of numbers and create a new array with each number converted into a string.
numbers = [1, 2, 3, 4, 5]
string_numbers = [str(number) for number in numbers]
print(string_numbers)
