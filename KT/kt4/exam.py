"""KT4."""


def odd_sums_of_consecutive_elements(nums: list) -> list:
    """Anime kruto."""
    res_list = []
    for ind, val in enumerate(nums):
        if ind != 0:
            sum = nums[ind] + nums[ind - 1]
            if sum % 2 != 0:
                res_list.append(sum)
        # print(nums[ind - 1])

    return res_list


def list_move(initial_list: list, amount: int, factor: int) -> list:
    """Anime kruto."""
    res_list = []
    if amount == 0:
        return []
    while amount != 0:
        res_list.append(initial_list)
        if len(initial_list) > 0:
            initial_list = initial_list[-int(factor) % len(initial_list):] + initial_list[:-int(factor) % len(initial_list)]
        else:
            initial_list = initial_list[-factor:] + initial_list[:-factor]
        amount -= 1
    return res_list


def fizzbuzz_series_up(nr: int) -> list:
    """Anime kruto."""
    res_list = []
    counter = 0
    if nr > 0:
        while nr != 0:
            counter += 1
            for i in range(1, counter + 1):
                res_list.append(i)
            nr -= 1
        for ind, val in enumerate(res_list):
            if (val % 3 == 0) and (val % 5 == 0):
                res_list[ind] = "fizzbuzz"
            else:
                if (val % 3 == 0):
                    res_list[ind] = "fizz"
                if (val % 5 == 0):
                    res_list[ind] = "buzz"
        return res_list
    else:
        return []
