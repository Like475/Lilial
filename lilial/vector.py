from matrix import Matrix2x2


class Vector2D():
    def __init__(self, coords: (tuple, list)):
        self.coords = tuple(coords)


class Vector2D():
    def __init__(self, coords: (tuple, list)):
        self.coords = tuple(coords)
    

    def __add__(self, other: Vector2D) -> Vector2D:
        if isinstance(other, Vector2D):
            return Vector2D((
                self.coords[0] + other.coords[0],
                self.coords[1] + other.coords[1]
            ))
        else:
            name_type = str(type(other)).split("'")[1]
            raise TypeError(f"unsupported operand type(s) for +: 'Vector2D' and '{name_type}'")
    

    def __mul__(self, other: (int, float, Matrix2x2)) -> Vector2D:
        if isinstance(other, (int, float)):
            return Vector2D((
                self.coords[0] * other,
                self.coords[1] * other
            ))
        elif isinstance(other, Matrix2x2):
            return Vector2D((
                other.data[0][0] * self.coords[0] + other.data[1][0] * self.coords[1],
                other.data[0][1] * self.coords[0] + other.data[1][1] * self.coords[1]
            ))
        else:
            name_type = str(type(other)).split("'")[1]
            raise TypeError(f"unsupported operand type(s) for *: 'Vector2D' and '{name_type}'")


i_2d_vector = Vector2D((1, 0))
j_2d_vector = Vector2D((0, 1))
