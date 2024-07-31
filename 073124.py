# Convert an array of arrays into a hash.
# For example, [[1, 3], [8, 9], [2, 16]] becomes {1 = > 3, 8 = > 9, 2 = > 16}.

array_of_arrays = [[1, 3], [8, 9], [2, 16]]
array_object = {}
for array in array_of_arrays:
    key = array[0]
    value = array[1]
    array_object[key] = value

print(array_object)

# Convert an array of hashes into a hash using the: id key from the array's hashes as the keys in the new hash.
# For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 = > {id: 1, color: "blue", price: 32}, 2 = > {id: 2, color: "red", price: 12}}.

array_of_objects = [
    {"id": 1, "color": "blue", "price": 32},
    {"id": 2, "color": "red", "price": 12}
]
object_of_objects = {}
for object in array_of_objects:
    key = object["id"]
    value = object
    object_of_objects[key] = value

print(object_of_objects)

# Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
# For example, "bookkeeper" becomes {"b" = > 1, "o" = > 2, "k" = > 2, "e" = > 3, "p" = > 1, "r" = > 1}.

string = "bookeeper"
letters_object = {}
for letter in string:
    if letter in letters_object:
        letters_object[letter] += 1
    else:
        letters_object[letter] = 1

print(letters_object)

# Convert a hash into an array of arrays.
# For example, {"chair" = > 100, "book" = > 14} becomes[["chair", 100], ["book", 14]].

items_object = {"chair": 100, "book": 14}
items_array = [[key, value] for key, value in items_object.items()]
print(items_array)


# Convert a hash into an array of hashes using the keys from each hash as the: id key in each of the array's hashes.
# For example, {321 = > {name: "Alice", age: 31}, 322 = > {name: "Maria", age: 27}} becomes[{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].

people_object = {
    321: {"name": "Alice", "age": 31},
    322: {"name": "Maria", "age": 27}
}
people_object_array = [
    {"id": key, **value}
    for key, value in people_object.items()
]
print(people_object_array)

# Convert an array of strings into a hash with keys for each string in the array and values for the number of times the string appears in the array.
# For example, ["do", "or", "do", "not"] becomes {"do" = > 2, "or" = > 1, "not" = > 1}.
word_array = ["do", "or", "do", "not"]
word_dictionary = {}
for word in word_array:
    if word in word_dictionary:
        word_dictionary[word] += 1
    else:
        word_dictionary[word] = 1

print(word_dictionary)

# Convert a hash into a flat array containing all the hash’s keys and values.
# For example, {"a" = > 1, "b" = > 2, "c" = > 3, "d" = > 4} becomes["a", 1, "b", 2, "c", 3, "d", 4].
letter_dictionary = {"a": 1, "b": 2, "c": 3, "d": 4}
letter_array = [
    element for key, value in letter_dictionary.items() for element in (key, value)
]
print(letter_array)
