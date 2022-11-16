"""."""

from abc import ABCMeta, abstractmethod


class TreeNode(metaclass=ABCMeta):
    """The main node class."""

    def __init__(self, *args):
        """:param make use of *args and store them in a way that it is easy to use them."""
        value0 = args[0]
        if isinstance(value0, tuple):
            self.left = value0[0]
            self.right = value0[1]
        else:
            self.value = value0

    @abstractmethod
    def apply(self):
        """abstract method which should be overridden to compute the value of the given abstract tree."""
        pass

    @abstractmethod
    def class_str(self):
        """:return class string representation of the object."""
        pass

    @abstractmethod
    def __str__(self):
        """:return string representation of the object."""
        pass

    def __eq__(self, other):
        """:return True when 2 object trees have the same shape and values."""
        return self.class_str() == other.class_str()

    def __ne__(self, other):
        """:return True when 2 object trees have a different shape and/or values."""
        return self.class_str() != other.class_str()
