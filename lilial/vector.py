from matrix import Matrix2x2


class Vector2d:
    """
    Vector in 2D space.
    When added it gives a new vector.
    When multiplied by a number it gives a new vector.
    When multiplied by a matrix it gives a new vector

    Parameters
    ----------
    coords : tuple or list
        The coordinates of the vector, they are the same scalars of i and j vectors
    """
    def __init__(self, coords: (tuple, list)):
        self.coords = tuple(coords)

    def __add__(self, other):
        if isinstance(other, Vector2d):
            return Vector2d((
                self.coords[0] + other.coords[0],
                self.coords[1] + other.coords[1]
            ))
        name_type = str(type(other)).split("'")[1]
        raise TypeError(f"unsupported operand type(s) for +: 'Vector2D' and '{name_type}'")

    def __mul__(self, other: (int, float, Matrix2x2)):
        if isinstance(other, (int, float)):
            return Vector2d((
                self.coords[0] * other,
                self.coords[1] * other
            ))
        elif isinstance(other, Matrix2x2):
            return Vector2d((
                other.data[0][0] * self.coords[0] + other.data[1][0] * self.coords[1],
                other.data[0][1] * self.coords[0] + other.data[1][1] * self.coords[1]
            ))
        name_type = str(type(other)).split("'")[1]
        raise TypeError(f"unsupported operand type(s) for *: 'Vector2D' and '{name_type}'")


i_2d_vector = Vector2d((1, 0))
j_2d_vector = Vector2d((0, 1))
