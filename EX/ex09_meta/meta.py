"""Meta-trees and meta-dragons."""

from turtle import Turtle
from sys import setrecursionlimit

setrecursionlimit(10000)


def tree(length):
    """See, mida tester tahab."""
    t = Turtle()
    if length >= 5:
        t.forward(length)
        t.left(60)  # suund left
        tree((length * 0.6))  # draw n*0.6 line
        t.right(120)
        tree((length * 0.6))
        t.left(60)
        t.back(length)  # liikume tagasi (jargmine trunk)


def apply_dragon_rules(string):
    """About the same thing that I used in last inception.py function."""
    result = ""
    try:
        if string[0] == "a":  # if letter is "a"
            result += "aRbFR"  # then add "aRbFR" into result string
        elif string[0] == "b":
            result += "LFaLb"
        else:
            result += string[0]
        newstr = string[1:]  # Remove first letter from string, which was used.
        result += apply_dragon_rules(newstr)

    except IndexError:
        pass
    return result


def curve(string, depth):
    """Mida tester tahab."""
    if depth != 0:
        return curve(apply_dragon_rules(string), depth - 1)
    else:
        return string


def format_curve(string):
    """Delete a and b letters from string."""
    if "a" in string:
        newstr = string.replace("a", "")
        return format_curve(newstr)
    elif "b" in string:
        newstr = string.replace("b", "")
        return format_curve(newstr)
    else:
        return string


def draw_dragon(string, length):
    """See, mida tester tahab."""
    t = Turtle()
    try:
        if string[0] == "L":  # Take first letter from string
            t.left(90)
            t.forward(length)
        elif string[0] == "R":
            t.right(90)
            t.forward(length)
        elif string[0] == "F":
            t.forward(length)
        newstr = string[1:]  # delete first letter from string, because it was used.

        draw_dragon(newstr, length)
    except IndexError:  # if IndexError (here no more letters)
        pass  # Ignore and don't do anything


def get_line_length(dragon_width, depth):
    """Return one Turtle step length if the width and depth are known."""
    return dragon_width / (2 ** (1 / 2)) ** depth


def save(t: Turtle):
    """Save the turtle graphic to file which can be opened with a image editor like GIMP."""
    t = Turtle()
    t.ht()  # hide him
    t.getscreen().getcanvas().postscript(file='tree.ps')
