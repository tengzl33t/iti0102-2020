"""."""

from abc import abstractmethod
from tree_node import TreeNode


class Operator(TreeNode):
    """Custom operation wrapper."""

    def __init__(self, *args):
        """Store the given arguments somehow."""
        super().__init__(*args)
        self.value = self.apply()

    def apply(self):
        """Make use of the *args to compute the value of the given subtree. Recursion is your friend."""
        return self.default_operator(self.left.apply(), self.right.apply())

    def class_str(self):
        """:return class string representation of the object."""
        return f"{self.__class__.__name__}({self.left.class_str()}, {self.right.class_str()})"

    def __str__(self):
        """:return the mathematical string representation of the tree with least amount of parenthesis."""
        print(self.left.__str__(), self.right.__str__())
        if self.default_operator.__str__() == "":
            return f"{self.__str__()}"
        elif hasattr(self.left, 'priority') and self.priority < self.left.priority:
            return f"({self.left.__str__()}) {self.default_operator.operand} {self.right.__str__()}"
        elif hasattr(self.right, 'priority') and self.priority == self.right.priority:
            return f"{self.left.__str__()} {self.default_operator.operand} ({self.right.__str__()})"
        else:
            return f"{self.left.__str__()} {self.default_operator.operand} {self.right.__str__()}"

    @property
    def associativity(self):
        """abstract method witch should be overridden to return a boolean when the node is not associative."""
        return False

    @property
    @abstractmethod
    def default_operator(self):
        """abstract method which should be overridden to return the default_operator object."""
        pass

    @property
    @abstractmethod
    def priority(self):
        """
        abstract method witch should be overridden to return priority of the node.

        Boolean whether the operation is associative or not.
        For example addition is associative but subtraction is not.
        Override this property for operations where the given operation is not associative.
        Visit: https://en.wikipedia.org/wiki/Order_of_operations
        """
        pass

    @property
    @abstractmethod
    def actions(self):
        """
        All custom implemented actions on different data structures.

        For example set - int does not exist, but we can implement it.
        :return a dictionary of functions where key is accepted parameters and value is a function which takes the
        aforementioned parameters as inputs and computes a value with them.
        """
        pass
