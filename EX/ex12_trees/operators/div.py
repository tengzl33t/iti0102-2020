"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Div(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))

    @property
    def priority(self):
        """priority of the operation."""
        return 3

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(self.actions[type(self.left.value), type(self.right.value)], "/")

    @property
    def actions(self):
        """:return a dictionary of custom operations."""
        return {
            (int, int): lambda x, y: x / y,  #
            (set, set): lambda x, y: x - y,  # set union
            (set, int): lambda x, y: x - {y},  # add to set
            (int, set): lambda x, y: y.remove({x})  # add to set
        }
