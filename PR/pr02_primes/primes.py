"""Sample text."""


def is_prime_number(number: int) -> bool:
    """Sample text."""
    if int(number) <= 1 or int(number) % 1 > 0:
        return False  # Vaatame kas number suurem kui 1 (1 ei ole prime number)
    for i in range(2, int(number)):  # Võtame number 2st kuni NUMBERni
        if int(number) % i == 0:  # Vaatame kas jaak on 0
            return False
    return True  # Paneme bool False kui jaak ei ole 0


if __name__ == '__main__':
    print(is_prime_number(2))
    print(is_prime_number(89))
    print(is_prime_number(23))
    print(is_prime_number(4))
    print(is_prime_number(7))
    print(is_prime_number(88))
    print(is_prime_number(3))
    print(is_prime_number(6073))
