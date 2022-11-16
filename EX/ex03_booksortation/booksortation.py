"""Booksortation."""


def booksortation(books: list) -> dict:
    """Sample text."""
    book_dict = {}
    book_result = []

    if books:
        for book in books:
            if is_spell_book(book) is True:
                add_book_to_category(book, "spell books", book_dict)

            elif is_history_book(book) is True:
                add_book_to_category(book, "history books", book_dict)

            elif is_relics_book(book) is True:
                add_book_to_category(book, "relics books", book_dict)

            elif is_potion_book(book) is True:
                add_book_to_category(book, "potion books", book_dict)

            else:
                add_book_to_category(book, "other books", book_dict)

    book_result = {i: sorted(book_dict[i], key=str.lower) for i in book_dict.keys()}

    return book_result


def add_book_to_category(book: str, category: str, categorised_books: dict) -> dict:
    """Sample text."""
    if category in categorised_books:
        categorised_books[category].append(book)
    else:
        categorised_books.setdefault(category, []).append(book)

    return categorised_books


def is_spell_book(book: str) -> bool:
    """Sample text."""
    if len(book) > 1:
        if book[0] == book[-1] == "*":
            return True
        else:
            return False
    else:
        return False


def is_history_book(book: str) -> bool:
    """Sample text."""
    split_book = book.split()

    if book != "":
        while len(split_book):
            for i in split_book:
                if i[0].islower():
                    return False
            else:
                return True
    else:
        return True


def is_relics_book(book: str) -> bool:
    """Sample text."""
    if book != "":
        for i in book:
            if i.isalpha() is True:
                check0 = True
            else:
                check0 = False

        if check0 is True:
            if book[0].islower():
                check1 = book[1::2].isupper()
                check2 = book[::2].islower()
            else:
                check1 = book[::2].isupper()
                check2 = book[1::2].islower()

            if (check1 and check2) is True:
                return True
            else:
                if len(book) > 1:
                    return False
                else:
                    return True
        else:
            swaped = book.swapcase()
            if swaped == book:
                return True
            else:
                return False
    else:
        return True


def is_potion_book(book: str) -> bool:
    """Sample text."""
    vowels = {"a", "e", "i", "o", "u"}
    consonants = {
        "b",
        "c",
        "d",
        "f",
        "g",
        "h",
        "j",
        "k",
        "l",
        "m",
        "n",
        "p",
        "q",
        "r",
        "s",
        "t",
        "v",
        "x",
        "z",
        "w",
        "y",
    }

    vow_count = 0
    con_count = 0
    lc_input = book.lower()

    for vowel in lc_input:
        if vowel in vowels:
            vow_count = vow_count + 1

    for consonant in lc_input:
        if consonant in consonants:
            con_count = con_count + 1

    if (
        con_count == vow_count
        or con_count - 1 == vow_count
        or con_count == vow_count - 1
    ):
        return True
    else:
        return False
