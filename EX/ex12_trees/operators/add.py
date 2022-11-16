"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Add(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))

    @property
    def priority(self):
        """:return the value of the operation."""
        return 4

    @property
    def default_operator(self):
        """:return the default operator of the operation."""
        return DefaultOperator(self.actions[type(self.left.value), type(self.right.value)], "+")
        #  go to the "actions"

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (int, int): lambda x, y: x + y,  # set union
            (set, set): lambda x, y: x.union(y),  # set union
            (set, int): lambda x, y: x.union({y}),  # add to set
            (int, set): lambda x, y: y.union({x})  # add to set
        }
