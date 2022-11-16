"""Test 2 (R10)."""


def format_time(minutes):
    """Sample text."""
    hours = minutes // 60

    minutesout = minutes % 60

    if hours < 1:
        result = str(minutesout) + "min"
    elif minutesout == 0 and hours > 0:
        result = str(hours) + "h"
    elif minutesout > 0 and hours > 0:
        result = str(hours) + "h " + str(minutesout) + "min"

    return result


def sorta_sum(a: int, b: int) -> int:
    """Sample text."""
    result = 0
    out = a + b
    sumrange = range(10, 20)

    if out in sumrange:
        result = 20
    else:
        result = out

    return result


def combo_string(s1: str, s2: str) -> str:
    """Sample text."""
    lens1 = len(s1)
    lens2 = len(s2)
    if lens1 < lens2:
        result = s1 + s2 + s1
    else:
        result = s2 + s1 + s2

    return result


def num_as_index(nums: list) -> int:
    """Sample text."""
    result = 0
    lastel = nums[-1]
    firstel = nums[0]
    maxlen = len(nums)
    if maxlen > 2:
        if (lastel > firstel) and firstel < maxlen:
            result = nums[firstel]
        elif (lastel < firstel) and lastel < maxlen:
            result = nums[lastel]
        elif lastel > maxlen and firstel > maxlen:
            result = nums[0]
    else:
        if lastel > firstel:
            result = firstel
        elif lastel < firstel:
            result = lastel
        elif lastel == firstel:
            result = firstel

    return result


print(num_as_index([0, 1]))  # == 0
print(num_as_index([1, 1]))  # == 1
print(num_as_index([77, 12]))  # == 12

# def count_clumps(nums: list) -> int:
#     """Sample text."""
#     counter = 0
#     countlist = []
#     for
#         if (item == nums[x-1]):

#             #print(nums[x - 1])
#             #print("----")
#             #print(nums[x])
#             #print(x)
#             counter = counter + 1

#     return counter

# #print(count_clumps([1, 2, 2, 3, 4, 4]))# → 2
# print(count_clumps([1, 1, 2, 1, 1]))# → 2
# print(count_clumps([1, 1, 1, 1, 1]))# → 1

# if __name__ == '__main__':
#     print(format_time(112))
#     print(sorta_sum(3, 4))
#     print(combo_string('Hello', 'hi'))
#     print(num_as_index([1, 2, 3]))
#     print(count_clumps([1, 2, 2, 3, 4, 4]))
