from vector import Vector2D, i_2d_vector, j_2d_vector


class LinearCombination2D():
    def __init__(self, a: Vector2D, b: Vector2D):
        self.a = a
        self.b = b
        self.vector = a + b
        if self.a.coords == (0, 0) and self.b.coords == (0, 0):
            self.span = 0
        else:
            a_ratio = 'zero_division' if self.a.coords[1] == 0 else self.a.coords[0] / self.a.coords[1]
            b_ratio = 'zero_division' if self.b.coords[1] == 0 else self.b.coords[0] / self.b.coords[1]
            if self.a.coords == (0, 0) or self.b.coords == (0, 0) or a_ratio == b_ratio:
                self.span = 1
            else:
                self.span = 2


basis_2d_linear_combination = LinearCombination2D(i_2d_vector, j_2d_vector)
