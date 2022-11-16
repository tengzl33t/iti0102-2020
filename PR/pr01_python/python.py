"""Sample text."""
py_age = 2008  # number with python age

name = input("What is your name? ")  # ask name and get answer from user
age = input(f"Hello, {name}! What year were you born in? ")  # ask age
real_age = int(py_age) - int(age)  # get age count (ex 2010-2008, user is 2 years old)
if real_age > 0:  # if user is older than python 3
    print(f"You were {real_age} years old when Python 3.0 was released.")
else:  # if user younger than python 3
    print(f"Python 3 was {abs(real_age)} years old when you were born.")
