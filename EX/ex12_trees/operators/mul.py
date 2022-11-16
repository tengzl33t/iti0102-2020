"""."""

from default_operator import DefaultOperator
from operators.operator import Operator
from tree_node import TreeNode


class Mul(Operator):
    """Custom operation."""

    def __init__(self, left: TreeNode, right: TreeNode):
        """default constructor."""
        super().__init__((left, right))

    @property
    def priority(self):
        """priority of the operation."""
        return 2

    @property
    def default_operator(self):
        """Make use of the 'operator' library or use a lambda function."""
        return DefaultOperator(self.actions[type(self.left.value), type(self.right.value)], "*")

    @property
    def actions(self):
        """:return a dictionary of custom operations. Make use of frozensets."""
        return {
            (int, int): lambda x, y: x * y,  #
            (set, set): lambda x, y: x.union(y),  # set union
            (set, int): lambda x, y: x.union({y}),  # add to set
            (int, set): lambda x, y: y.union({x})  # add to set
        }
