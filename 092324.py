# Use a nested loop to convert an array of number pairs into a single flattened array.
# For example, [[1, 3], [8, 9], [2, 16]] becomes[1, 3, 8, 9, 2, 16].

nested_pairs = [[1, 3], [8, 9], [2, 16]]
flattened_pairs = [number for pair in nested_pairs for number in pair]
print(flattened_pairs)

# Use a nested loop with two arrays of strings to create a new array of strings with each string combined.
# For example, ["a", "b", "c"] and ["d", "e", "f", "g"] becomes["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"].

letters1 = ["a", "b", "c"]
letters2 = ["d", "e", "f", "g"]
combined_letters = [
    letter1 + letter2 for letter1 in letters1 for letter2 in letters2
]
print(combined_letters)

# Use a nested loop with one array of strings to create a new array that contains every combination of each string with every other string in the array.
# For example, ["a", "b", "c", "d"] becomes["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"].

letters = ["a", "b", "c", "d"]
conjoined_letters = [
    letter1 + letter2 for letter1 in letters for letter2 in letters if letter1 != letter2
]
print(conjoined_letters)

# Use a nested loop to find the largest product of any two different numbers within a given array.
# For example, [5, -2, 1, -9, -7, 2, 6] becomes 63.

numbers = [5, -2, 1, -9, -7, 2, 6]
largest_product = max(
    number1 * number2 for number1 in numbers for number2 in numbers if number1 != number2
)
print(largest_product)

# Use a nested loop to compute the sum of all the numbers in an array of number pairs.
# For example, [[1, 3], [8, 9], [2, 16]] becomes 39.

nested_numbers = [[1, 3], [8, 9], [2, 16]]
sum_of_numbers = sum(number for pair in nested_numbers for number in pair)
print(sum_of_numbers)

# Use a nested loop with two arrays of numbers to create a new array of the sums of each combination of numbers.
# For example, [1, 2] and [6, 7, 8] becomes[7, 8, 9, 8, 9, 10].

numbers1 = [1, 2]
numbers2 = [6, 7, 8]
sum_array = [number1 + number2 for number1 in numbers1 for number2 in numbers2]
print(sum_array)

# Use a nested loop with an array of numbers to compute an array with every combination of products from each number.
# For example, [2, 8, 3] becomes[4, 16, 6, 16, 64, 24, 6, 24, 9].

numbers = [2, 8, 3]
possible_products = [
    number1 * number2 for number1 in numbers for number2 in numbers
]
print(possible_products)

# Use a nested loop to find the largest sum of any two different numbers within an array.
# For example, [1, 8, 3, 10] becomes 18.

numbers = [1, 8, 3, 10]
largest_sum = max(
    number1 + number2 for number1 in numbers for number2 in numbers if number1 != number2
)
print(largest_sum)

# Use nested loops with an array of numbers to compute a new array containing the first two numbers(from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.
# For example, [2, 5, 3, 1, 0, 7, 11] becomes[3, 7].

numbers = [2, 5, 3, 1, 0, 7, 11, 5, 11, 2]
seen = set()

for number in numbers:
    compliment = 10 - number
    if compliment in seen or (compliment == number and numbers.count(number) > 1):
        print([number, compliment])
        break
    seen.add(number)
else:
    print(False)

# Use a nested loop to convert an array of string arrays into a single string.
# For example, [["a", "man"], ["a", "plan"], ["a", "canal"], ["panama"]] becomes "amanaplanacanalpanama".

string_components = [
    ["a", "man"],
    ["a", "plan"],
    ["a", "canal"],
    ["panama"]
]

palindrome = "".join(word for words in string_components for word in words)
print(palindrome)
