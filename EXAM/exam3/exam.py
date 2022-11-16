"""Eksam 3 (2020-01-12)."""


def odd_index_sum(nums: list) -> int:
    """Sample text."""
    res_list = []
    for i, n in enumerate(nums):
        if i % 2 != 0:
            res_list.append(n)
    return sum(res_list)


def encode_string_with_hex_key(input_str: str, key: str) -> str:
    """Sample text."""
    letters_low = "abcdefghijklmnopqrstuvwxyz"  # 26 chars
    letters_high = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    hex_letters = {"a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15}

    dec_letters = ""
    try:
        for i, v in enumerate(key):
            if v.isdecimal():
                key_int = v
            else:
                key_int = hex_letters[v]

            if input_str[i].isalpha():
                if input_str[i].isupper():
                    old_index = letters_high.index(input_str[i])
                    new_index = (old_index + int(key_int)) % 26
                    dec_letters += letters_high[new_index]
                else:
                    old_index = letters_low.index(input_str[i])
                    new_index = (old_index + int(key_int)) % 26
                    dec_letters += letters_low[new_index]
            else:
                dec_letters += input_str[i]

        return dec_letters
    except IndexError:
        return input_str


def who_gets_gingerbread(students: dict, total_gingerbreads: int) -> dict:
    """Sample text."""
    new_dict = {}
    for k, v in students.items():
        if v > 2.0:
            new_dict[k] = v

    sort_by_grade = sorted(new_dict, key=new_dict.get, reverse=True)
    res_dict = {}
    for i in sort_by_grade:
        res_dict[i] = 0

    while total_gingerbreads > 0:
        for i in sort_by_grade:
            if total_gingerbreads > 0:
                res_dict[i] += 1
                total_gingerbreads -= 1

    res1_dict = {}

    for k, v in res_dict.items():
        if v >= 1:
            res1_dict[k] = v

    return res1_dict


def convert_list(input_list: list):
    """Sample text."""
    raise TypeError()


def make_table(n: int):
    r"""
    Given an odd integer n, return a n*n table like shown in the examples.

    #5

    The given n is more or equal to 7.

    Example 1:
    n=15
    result:

    \#####/|\#####/
    #\###/#|#\###/#
    ##\#/##|##\#/##
    ###X###|###X###
    ##/#\##|##/#\##
    #/###\#|#/###\#
    /#####\|/#####\
    -------+-------
    \#####/|\#####/
    #\###/#|#\###/#
    ##\#/##|##\#/##
    ###X###|###X###
    ##/#\##|##/#\##
    #/###\#|#/###\#
    /#####\|/#####\

    Example 2:
    n=7
    result:

    \#/|\#/
    #X#|#X#
    /#\|/#\
    ---+---
    \#/|\#/
    #X#|#X#
    /#\|/#\

    Example 3:
    n=9
    result:

    \##/|\##/
    #\/#|#\/#
    #/\#|#/\#
    /##\|/##\
    ----+----
    \##/|\##/
    #\/#|#\/#
    #/\#|#/\#
    /##\|/##\

    :return:
    """
    pass


class Student:
    """Represent student model."""

    def __init__(self, name: str, gpa: float, age: int):
        """Sample text."""
        self.age = age
        self.gpa = gpa
        self.name = name


class University:
    """Represent university model."""

    def __init__(self, name: str, gpa_required: float):
        """Sample text."""
        self.name = name
        self.gpa_required = gpa_required
        self.students_list = []

    def can_enroll_student(self, student: Student) -> bool:
        """Sample text."""
        if student.age >= 16 and (
                student.gpa >= self.gpa_required or len(student.name) == 13) and student not in self.students_list:
            return True
        else:
            return False

    def enroll_student(self, student: Student):
        """Sample text."""
        if self.can_enroll_student(student):
            self.students_list.append(student)

    def can_unenroll_student(self, student: Student) -> bool:
        """Sample text."""
        if student in self.students_list:
            return True
        else:
            return False

    def unenroll_student(self, student: Student):
        """Sample text."""
        if self.can_unenroll_student(student):
            self.students_list.remove(student)

    def get_students(self) -> list:
        """Sample text."""
        return self.students_list

    def get_student_highest_gpa(self) -> list:
        """Sample text."""
        gpa_sort = sorted(self.students_list, key=lambda x: -x.gpa)
        student_list = []

        if gpa_sort != []:

            max_gpa = gpa_sort[0].gpa

            for i in gpa_sort:
                if i.gpa == max_gpa:
                    student_list.append(i)

        return student_list


class Accessory:
    """Accessory."""

    def __init__(self, name: str, value: int):
        """Constructor."""
        self.name = name
        self.value = value

    def __repr__(self):
        """Sample text."""
        return f"{self.name}, value : {self.value}."


class Car:
    """Car."""

    def __init__(self, name: str, color: str):
        """Constructor."""
        self.name = name
        self.color = color
        self.accessories = []
        self.premium = False
        self.fuel = 100
        # self.value = 0

    def make_premium(self):
        """Sample text."""
        self.premium = True

    def add_accessory(self, accessory: Accessory):
        """Add accessory to the car."""
        self.accessories.append(accessory)

    def get_value(self) -> int:
        """Sample text."""
        accessory_sum = sum([i.value for i in self.accessories])

        if self.premium:
            return 42500 + accessory_sum
        else:
            return 9500 + accessory_sum

    def use_fuel(self, count):
        """Sample text."""
        self.fuel -= count

    def get_fuel_left(self):
        """Return how much fuel is left in percentage."""
        return self.fuel

    def get_accessories_by_value(self):
        """Return accessories sorted by value (descending i.e. higher to lower)."""
        return sorted(self.accessories, key=lambda x: -x.value)

    def __repr__(self):
        """Sample text."""
        return f"This {self.color} {self.name} contains {len(self.accessories)} accessories and has {self.fuel}% fuel left."


class Customer:
    """Customer."""

    def __init__(self, name: str, wish: str):
        """Sample text."""
        splitted_wish = wish.split(" ")
        self.name = name
        self.wish_value = splitted_wish[0]
        self.wish_color = splitted_wish[1]
        self.garage = []
        self.premium = False

    def get_garage(self):
        """Sample text."""
        return sorted(self.garage, key=lambda x: x.get_value())

    def make_premium(self):
        """Make customer a premium customer, premium cars can be sold to the customer now."""
        self.premium = True

    def drive_with_car(self, driving_style: str):
        """Sample text."""
        if self.garage != []:

            most_fuel = sorted(self.garage, key=lambda x: -x.fuel)[0]
            most_value = sorted(self.garage, key=lambda x: -x.get_value())
            max_fuel_level = most_fuel.fuel

            car_list = []
            for i in most_value:
                if i.fuel == max_fuel_level:
                    car_list.append(i)

            useful_car = car_list[0]

            if driving_style == "Rally":
                most_value[-1].use_fuel(35)
            else:
                useful_car.use_fuel(15)

            if useful_car.get_fuel_left() <= 0:
                self.garage.remove(useful_car)


class Dealership:
    """Dealership."""

    def __init__(self, name: str):
        """Constructor."""
        self.name = name
        self.cars = []

    def add_car(self, car: Car):
        """Car is added to dealership."""
        self.cars.append(car)

    def get_all_regular_cars(self):
        """Return all the regular cars sorted by value (ascending, lower to higher)."""
        srtd = sorted(self.cars, key=lambda x: x.get_value())
        res_list = []
        for i in srtd:
            if not i.premium:
                res_list.append(i)
        return res_list

    def make_car_premium(self, car: Car):
        """Make a car premium, which can can be sold only to premium customers."""
        car.make_premium()

    def get_all_premium_cars(self):
        """Return all the premium cars sorted by value (ascending, lower to higher)."""
        srtd = sorted(self.cars, key=lambda x: x.get_value())
        res_list = []
        for i in srtd:
            if i.premium:
                res_list.append(i)
        return res_list

    def sell_car_to_customer(self, customer: Customer):
        """Sample text."""
        if customer.wish_value == "Cheap":
            if customer.premium:
                car_to_sell = self.get_all_premium_cars()[0]
            else:
                car_to_sell = self.get_all_regular_cars()[0]
        else:
            if customer.premium:
                car_to_sell = self.get_all_premium_cars()[-1]
            else:
                car_to_sell = self.get_all_regular_cars()[-1]

        customer.garage.append(car_to_sell)
        self.cars.remove(car_to_sell)
