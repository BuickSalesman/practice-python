# Start with an array of numbers and create a new array with each number times 3.
# For example, [1, 2, 3] becomes[3, 6, 9].

numbers = [1, 2, 3]
trippled_numbers = [number * 3 for number in numbers]
print(trippled_numbers)

# Start with an array of strings and create a new array with each string upcased.
# For example, ["hello", "goodbye"] becomes["HELLO", "GOODBYE"].

words = ["hello", "goodbye"]
capital_words = [word.upper() for word in words]
print(capital_words)

# Start with an array of hashes and create a new array of string values from each hash's: name key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes["Alice", "Blane"].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
names = [person["name"] for person in people]
print(names)

# Start with an array of numbers and create a new array with each number plus 7.
# For example, [1, 2, 3] becomes[8, 9, 10].

numbers = [1, 2, 3]
slightly_bigger_numbers = [number + 7 for number in numbers]
print(slightly_bigger_numbers)

# Start with an array of strings and create a new array with each string's length.
# For example, ["hello", "goodbye"] becomes[5, 7].

words = ["hello", "goodbye"]
words_length = [len(word) for word in words]
print(words_length)

# Start with an array of hashes and create a new array of number values from each hash's: age key.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes[27, 16].

people = [{"name": "Alice", "age": 27}, {"name": "Blane", "age": 16}]
ages = [person["age"] for person in people]
print(ages)


# Start with an array of numbers and create a new array with each number divided by 2.
# For example, [1, 2, 3] becomes[0.5, 1.0, 1.5].

divided = [number / 2 for number in numbers]
print(divided)

# Start with an array of strings and create a new array with each string's first letter only.
# For example, ["hello", "goodbye"] becomes["h", "g"].

first_letter = [word[0] for word in words]
print(first_letter)

# Start with an array of hashes and create a new array of number values from each hash's: age key times 2.
# For example, [{name: "Alice", age: 27}, {name: "Blane", age: 16}] becomes[54, 32].

multiplied_ages = [person["age"] * 2 for person in people]
print(multiplied_ages)

# Start with an array of numbers and create a new array with each number converted into a string.
# For example, [1, 2, 3] becomes["1", "2", "3"].

numbers = [1, 2, 3]
stringy_numbers = [str(number) for number in numbers]
print(stringy_numbers)
