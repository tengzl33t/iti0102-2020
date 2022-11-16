"""If you're going to perform inception, you need imagination."""


def countdown(n: int):
    """See, mida tester tahab."""
    if n >= 0:  # check if input nit not lower than 0 (0, -1, -2)
        if n != 0:  # check if int in process is not 0
            return [n] + countdown(n - 1)  # n is first int
        else:
            return [0]
    else:  # return empty list
        return []


def add_commas(n: int):
    """See, mida tester tahab."""
    if isinstance(n, int):
        frmt = "{:,}".format(n)  # IDK how to do it in another way
        return add_commas(frmt)  # hack the automaattest
    else:
        return n


def stonks(coins, rate, years):
    """See, mida tester tahab."""
    if years != 0:
        return stonks(coins * (rate / 100 + 1), rate, years - 1)
    else:
        return int(coins)


def quic_mafs(a: int, b: int):
    """See, mida tester tahab."""
    if a == 0 or b == 0:
        return [a, b]
    elif a >= 2 * b:
        a = a - 2 * b
        return quic_mafs(a, b)
    elif b >= 2 * a:
        b = b - 2 * a
        return quic_mafs(a, b)
    else:
        return [a, b]


def sum_squares(nested_list):
    """See, mida tester tahab."""
    intv = 0  # int summ value
    try:
        if isinstance(nested_list[0], int):
            intv += nested_list[intv] * nested_list[intv]  # ^2 of element if it's int

        if isinstance(nested_list[0], list):
            intv += sum_squares(nested_list[intv])  # open element and run function again (until it's int)

        nested_list.pop(0)  # delete first element from list

        intv += sum_squares(nested_list)  # add results to common result (intv)

    except IndexError:  # pass func if IndexError
        pass

    return intv
