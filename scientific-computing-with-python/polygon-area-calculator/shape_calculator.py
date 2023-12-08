"""
@name: shape_calculator.py
@date: 07/11/2023 (dd/mm/yy)
@author: github.com/chrvstian
"""


class Rectangle:
  """A class representing a rectangle."""

  def __init__(self, width, height):
    """Initialize the Rectangle with specified width and height."""
    self.width = width
    self.height = height

  def set_width(self, width):
    """Set the width of the rectangle."""
    self.width = width

  def set_height(self, height):
    """Set the height of the rectangle."""
    self.height = height

  def get_area(self):
    """Calculate and return the area of the rectangle."""
    return self.width * self.height

  def get_perimeter(self):
    """Calculate and return the perimeter of the rectangle."""
    return 2 * self.width + 2 * self.height

  def get_diagonal(self):
    """Calculate and return the diagonal of the rectangle."""
    return (self.width**2 + self.height**2)**0.5

  def get_picture(self):
    """Return a string representing the shape using '*' characters."""
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    return ('*' * self.width + '\n') * self.height

  def get_amount_inside(self, shape):
    """Calculate and return the number of times the passed shape can fit inside."""
    return (self.width // shape.width) * (self.height // shape.height)

  def __str__(self):
    """Return a string representation of the Rectangle instance."""
    return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
  """A class representing a square, which is a subclass of Rectangle."""

  def __init__(self, side):
    """Initialize the Square with a side length."""
    super().__init__(side, side)

  def set_side(self, side):
    """Set the side length of the square."""
    self.width = side
    self.height = side

  def set_width(self, width):
    """Set the width of the square."""
    self.set_side(width)

  def set_height(self, height):
    """Set the height of the square."""
    self.set_side(height)

  def __str__(self):
    """Return a string representation of the Square instance."""
    return f"Square(side={self.width})"
