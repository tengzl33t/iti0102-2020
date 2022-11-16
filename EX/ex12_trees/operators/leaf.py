"""."""

from tree_node import TreeNode


class Leaf(TreeNode):
    """Leaf node."""

    def __init__(self, value):
        """default constructor."""
        super().__init__(value)
        self.value = value

    def apply(self):
        """:return the value."""
        return self.value

    def class_str(self):
        """:return class string representation of the object."""
        return f"Leaf({self.value})"

    def __str__(self):
        """return string format of value."""
        return str(self.value)
