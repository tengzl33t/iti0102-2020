"""Shapes."""


class Shape:
    """General shape class."""

    def __init__(self, color: str):
        """Constructor, sets the color."""
        self._color = color
        pass

    def set_color(self, color: str):
        """Set the color of the shape."""
        self._color = color
        pass

    def get_color(self) -> str:
        """Get the color of the shape."""
        return self._color

    def get_area(self) -> float:
        """Get area method which every subclass has to override."""
        print("Implement area")
        pass


class Circle(Shape):
    """Circle is a subclass of Shape."""

    def __init__(self, color: str, radius: float):
        """Sample text."""
        super().__init__(color)
        self._radius = radius
        pass

    def __repr__(self) -> str:
        """Sample text."""
        return f"Circle (r: {self._radius}, color: {self._color})"

    def get_area(self) -> float:
        """Sample text."""
        return 3.14 * (self._radius * self._radius)


class Square(Shape):
    """Square is a subclass of Shape."""

    def __init__(self, color: str, side: float):
        """Sample text."""
        super().__init__(color)
        self._side = side
        pass

    def __repr__(self) -> str:
        """Sample text."""
        return f"Square (a: {self._side}, color: {self._color})"

    def get_area(self) -> float:
        """Sample text."""
        return self._side * self._side


class Rectangle(Shape):
    """Sample text."""

    def __init__(self, color: str, length: float, width: float):
        """Sample text."""
        super().__init__(color)
        self._length = length
        self._width = width
        pass

    def __repr__(self) -> str:
        """Sample text."""
        return f"Rectangle (l: {self._length}, w: {self._width}, color: {self._color})"

    def get_area(self) -> float:
        """Sample text."""
        return self._length * self._width


class Paint:
    """The main program to manipulate the shapes."""

    def __init__(self):
        """Constructor should create a list to store all the shapes."""
        self.paint_list = []
        pass

    def add_shape(self, shape: Shape) -> None:
        """Add a shape to the program."""
        self.paint_list.append(shape)
        pass

    def get_shapes(self) -> list:
        """Sample text."""
        return self.paint_list

    def calculate_total_area(self) -> float:
        """Sample text."""
        res = 0
        for i in self.get_shapes():
            res += i.get_area()
        return res

    def get_circles(self) -> list:
        """Sample text."""
        res_list = []
        for i in self.get_shapes():
            if isinstance(i, Circle):
                res_list.append(i)
        return res_list

    def get_squares(self) -> list:
        """Return only squares."""
        res_list = []
        for i in self.get_shapes():
            if isinstance(i, Square):
                res_list.append(i)
        return res_list

    def get_rectangles(self) -> list:
        """Return only rectangles."""
        res_list = []
        for i in self.get_shapes():
            if isinstance(i, Rectangle):
                res_list.append(i)
        return res_list
