"""Custom wrapper for function with a string representation."""


class DefaultOperator:
    """Default operator is a wrapper to a mathematical function with a string form."""

    def __init__(self, data_func, operand):
        """Võib olla siin on midagi huvitav."""
        self.data_func = data_func  # function lambda x, y
        self.operand = operand  # operator (+, -, *, etc)

    def __call__(self, *args, **kwargs):
        """Võib olla siin on midagi huvitav."""
        return self.data_func(args[0], args[1])  # data_func returns result of function lambda with 2 arguments (x, y)

    def __str__(self):
        """Võib olla siin on midagi huvitav."""
        return self.operand
