"""KT2."""


def sum_elements_around_last_three(nums: list) -> int:
    """
    Given a list of ints.

    Find sum of elements before and after last 3 in the list.

    If there is no 3 in the list or list is too short
    or there is no element before or after last 3 return 0.

    Note if 3 is last element in the list you must return
    sum of elements before and after 3 which is before last.


    sum_before_and_after_last_three([1, 3, 7]) -> 8
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]) -> 9
    sum_before_and_after_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]) -> 5
    sum_before_and_after_last_three([1, 2, 3]) -> 0

    :param nums: given list of ints
    :return: sum of elements before and after last 3
    """

    if 3 in nums:
        last3 = len(nums) - 1 - nums[::-1].index(3)
        if len(nums) >= 3:
            if nums[last3] == nums[0]:
                return 0
            if nums[last3] == nums[-1] and len(nums) == 3:
                return 0
            else:
                if nums[last3] != nums[-1]:
                    return sum([nums[last3 - 1], nums[last3 + 1]])
                else:
                    return sum([nums[last3 - 1], nums[last3 - 2]])
        else:
            return 0
    else:
        return 0

print(sum_elements_around_last_three([1, 3, 7]))
print(sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 4, 5, 6]))
print(sum_elements_around_last_three([1, 2, 3, 4, 6, 4, 3, 4, 5, 3, 3, 2, 3]))
print(sum_elements_around_last_three([1, 2]))
print(sum_elements_around_last_three([3, 4, 5, 6, 7, 0, 3]))
print("-------------------------")

def has_seven(nums: list):
    """
    Given a list if ints, return True if the value 7 appears in the list exactly 3 times
    and no consecutive elements have the same value.

    has_seven([1, 2, 3]) => False
    has_seven([7, 1, 7, 7]) => False
    has_seven([7, 1, 7, 1, 7]) => True
    has_seven([7, 1, 7, 1, 1, 7]) => False
    """
    count7 = nums.count(7)
    exlist = []
    #print(count7)
    if count7 >= 3:
        for index, i in enumerate(nums):
            if i != 7:
                exlist.append(nums.count(i))
        if nums[index] is nums[index - 1]:
            return False
        if count7 not in exlist:
            return True
        else:
            return False
    else:
        return False


print(has_seven([1, 2, 3])) # => False
print(has_seven([7, 1, 7, 7])) # => False
print(has_seven([7, 1, 7, 1, 7])) # => True
print(has_seven([7, 1, 7, 1, 1, 7])) # => False)
print("-------------------------")

def g_happy(s: str):
    """
    We'll say that a lowercase 'g' in a string is "happy" if there is another 'g' immediately to its left or right.

    Return True if all the g's in the given string are happy.

    g_happy("xxggxx") => True
    g_happy("xxgxx") => False
    g_happy("xxggyygxx") => False
    """
    for i in range(len(s)):
        if s[i] == "g" and s[i] == [-1]:
            if s[i] == "g" and s[i - 1] == "g":
                return True
        else:
            if s[i] == "g" and (s[i - 1] == "g" or s[i + 1] == "g"):
                return True
    return False


print(g_happy("xxggxx"))  # True
print(g_happy("xxgxx"))  # False
print(g_happy("xxggyygxx"))  # False


class Book:
    """Book object."""

    def __init__(self, name: str, pages: int, publish_year: int):
        """Book constructor."""
        self.name = name
        self.publish_year = publish_year
        self.pages = pages


def shorten_book_names(books: list, length: int):
    """
    Modify given list so that all objects' names are shorter or equal to given length.

    If name is longer than length then it must be shortened with 3 dots.
    Example, length = 10:
    "Algorithm Design" => "Algorit..."
    "Clean Code" => "Clean Code"

    :param books: input list
    :param length: max length for name (including dots)
    """
    for indx, item in enumerate(books):
        if len(item) >= length:
            books[indx] = item[0:length] + "..."
    return books

#print(shorten_book_names(["Algorithm Design", "Clean Code"], 10))


def convert_to_list_of_dicts(books: list) -> list:
    """
    Get list of dictionaries where key is hard-coded string
    and value is object's relevant variable.

    Example:
    {"name": "Clean Code", "publish_year": 2008, "pages": 464}

    :param books: input list
    :return: list of dictionaries, e.g. [{...}, {...}]
    """
    pass


def get_books_in_year(books: list, year: int) -> list:
    """
    Get all books that were published in the given year.

    :param books: input list
    :param year: publish year
    :return: new list with books in given year
    """
    pass


def sort_books(books: list) -> list:
    """
    Sort books by their name, publish year and pages in ascending order.

    :param books: input list
    :return: new sorted list of books
    """
    pass


def sort_by_name_length(books: list) -> list:
    """
    Sort books by their name length in descending order.

    :param books: input list
    :return: new sorted list of books
    """
    pass


class Robot:
    """Robot."""

    def __init__(self, name: str):
        """Contstructor."""
        pass

    def get_name(self) -> str:
        """Return robot name."""
        pass

    def calculate_price(self) -> int:
        """
        Calculate robot price.

        Robot's price is the sum of the ASCII value of every individual letter in it's name (first 3 letters) and the
        value of it's name's last 2 digits.
        You can and should use ord() function to get the ASCII value of a character. ord("A") = 65, ord("B") = 66, ...
        example: "ABF18" => 65 + 66 + 70 + 18 = 219
        """
        pass

    def __repr__(self) -> str:
        """String representation of the robot."""
        pass


class Factory:
    """Factory."""

    def __init__(self, factory_id: str):
        """Constructor."""
        pass

    def get_robots_in_factory(self) -> list:
        """Return robots in the factory as a list."""
        pass

    def get_factory_id(self) -> str:
        """Return the factory id."""
        pass

    def add_robot(self, robot: Robot) -> Robot:
        """
        Add a robot to the factory.

        Robot is only added to the factory if a robot with the same name does not already exist within this factory.
        """
        pass

    def generate_robot_factory_name(self) -> str:
        """
        Generate unique name.

        Name is generated RANDOMLY and must follow pattern:
        "<factory_id><uppercase_Ascii_letter><integer><integer>".
        For an empty(no robots) factory with id AB valid id examples are : [ABF18,ABP63,ABG51,...].
        this function can not generate the same name twice!
        return the name generated.
        """
        pass

    def get_remaining_robot_names_count(self) -> int:
        """
        Return how many new robots factory can make.

        Factory can not make a robot, if every name is generated.
        The amount of robots the factory can make is equal to the amount of names the factory can generate.
        """
        pass

    def make_robot(self) -> Robot:
        """
        Make a new robot in the factory.

        Robot's name must be unique within this factory and follow pattern:
        "<factory_id><uppercase_Ascii_letter><random integer><random integer>".
        Add the robot to the factory.
        Return made robot.
        """
        pass

    def get_sorted_robots_in_factory(self) -> list:
        """Get robots in factory sorted by their price in non-decreasing order."""
        pass

    def get_highest_priced_robot_in_factory(self) -> Robot:
        """Get the highest priced robot within factory."""
        pass

    def __repr__(self) -> str:
        """String representation of the factory."""
        pass
