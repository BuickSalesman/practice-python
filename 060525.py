def sum_odds(nums: List[int]) -> int:
    numsum = 0
    for num in nums:
        if num % 2 != 0:
            numsum += num

    return numsum


def contains_duplicate(nums: List[int]) -> bool:
    numset = set()
    for num in nums:
        if num in numset:
            return True
        numset.add(num)

    return False


def two_sum(nums: List[int], target: int) -> List[int]:
    seen = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in seen:
            return [seen[c], i]
        seen[num] = i
