def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))


def largest_in_list(numbers):
    return max(numbers)


def is_palindrome(s):
    return s == s[::-1]


def count_vowels(s):
    vowels = set("aeiouAEIOU")
    return sum(char in vowels for char in s)


def generate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]

    fib = [0, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib


def squares_1_to_10():
    return [x*x for x in range(1, 11)]


def unique_elements(lst):
    return list(set(lst))


def reverse_list_in_place(lst):
    left, right = 0, len(lst) - 1
    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def merge_dicts(d1, d2):
    merged = d1.copy()
    merged.update(d2)
    return merged
