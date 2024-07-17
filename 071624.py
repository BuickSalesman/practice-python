# Use a nested loop to convert an array of number pairs into a single flattened array.
# For example, [[1, 3], [8, 9], [2, 16]] becomes [1, 3, 8, 9, 2, 16].

array_of_pairs = [[1, 3], [8, 9], [2, 16]]
flatened_array = []

for pair in array_of_pairs:
    flatened_array += pair

print(flatened_array)

# Use a nested loop with two arrays of strings to create a new array of strings with each string combined.
# For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].

letters1 = ["a", "b", "c"]
letters2 = ["d", "e", "f", "g"]
combined_letters = []


for letter1 in letters1:
    combined_letters += [letter1 + letter2 for letter2 in letters2]


print(combined_letters)


# Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
# For example, ["a", "b", "c", "d"] becomes ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].

letters = ["a", "b", "c", "d"]
combined_letters = [
    letter1 + letter2 for letter1 in letters for letter2 in letters if letter1 != letter2
]


print(combined_letters)
