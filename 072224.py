# Convert an array of arrays into a hash.
# For example, [[1, 3], [8, 9], [2, 16]] becomes {1 => 3, 8 => 9, 2 => 16}.

number_arrays = [[1, 3], [8, 9], [2, 16]]
numbers_object = {}
for pair in number_arrays:
    key = pair[0]
    value = pair[1]
    numbers_object[key] = value

print(numbers_object)

# Convert an array of hashes into a hash using the :id key from the array's hashes as the keys in the new hash.
# For example, [{id: 1, color: "blue", price: 32}, {id: 2, color: "red", price: 12}] becomes {1 => {id: 1, color: "blue", price: 32}, 2 => {id: 2, color: "red", price: 12}}.

object_array = [
    {"id": 1, "color": "blue", "price": 32},
    {"id": 2, "color": "red", "price": 12}
]
object_object = {}

for object in object_array:
    key = object["id"]
    value = object
    object_object[key] = value

print(object_object)

# Convert a string into a hash with keys for each letter in the string and values for the number of times the letter appears in the string.
# For example, "bookkeeper" becomes {"b" => 1, "o" => 2, "k" => 2, "e" => 3, "p" => 1, "r" => 1}.

string = "bookkeeper"
string_object = {}

for letter in string:
    if letter in string_object:
        string_object[letter] += 1
    else:
        string_object[letter] = 1


print(string_object)

# Convert a hash into an array of arrays.
# For example, {"chair" => 100, "book" => 14} becomes [["chair", 100], ["book", 14]].

object = {"chair": 100, "book": 14}

array_of_arrays = [[key, value] for key, value in object.items()]

print(array_of_arrays)


# Convert a hash into an array of hashes using the keys from each hash as the :id key in each of the array's hashes.
# For example, {321 => {name: "Alice", age: 31}, 322 => {name: "Maria", age: 27}} becomes [{id: 321, name: "Alice", age: 31}, {id: 322, name: "Maria", age: 27}].

people_object = {
    321: {"name": "Alice", "age": 31},
    322: {"name": "Maria", "age": 27}
}
array_of_people_objects = [
    {"id": id, **details} for id, details in people_object.items()
]

print(array_of_people_objects)

# Convert an array of strings into a hash with keys for each string in the array and values for the number of times the string appears in the array.
# For example, ["do", "or", "do", "not"] becomes {"do" => 2, "or" => 1, "not" => 1}.

string_array = ["do", "or", "do", "not"]
string_object = {}
for string in string_array:
    if string in string_object:
        string_object[string] += 1
    else:
        string_object[string] = 1

print(string_object)

# Convert a hash into a flat array containing all the hash’s keys and values.
# For example, {"a" => 1, "b" => 2, "c" => 3, "d" => 4} becomes ["a", 1, "b", 2, "c", 3, "d", 4].

letters_object = {"a": 1, "b": 2, "c": 3, "d": 4}
letters_array = []

for key, value in letters_object.items():
    letters_array.append(key)
    letters_array.append(value)

print(letters_array)

# Given a hash, create a new hash that has the keys and values switched.
# For example, {"a" => 1, "b" => 2, "c" => 3} becomes {1 => "a", 2 => "b", 3 => "c"}.

unflipped_object = {"a": 1, "b": 2, "c": 3}
flipped_object = {value: key for key, value in unflipped_object.items()}
print(flipped_object)
