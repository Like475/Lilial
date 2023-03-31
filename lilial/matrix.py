class Matrix2x2():
    def __init__(self, data: (tuple, list)):
        self.data = (
            (data[0][0], data[0][1]),
            (data[1][0], data[1][1])
        )


class Matrix2x2():
    def __init__(self, data: (tuple, list)):
        self.data = (
            (data[0][0], data[0][1]),
            (data[1][0], data[1][1])
        )
    

    def mul(self, other: Matrix2x2) -> Matrix2x2:
        return Matrix2x2((
            (
                other.data[0][0] * self.data[0][0] + other.data[1][0] * self.data[0][1],
                other.data[0][1] * self.data[0][0] + other.data[1][1] * self.data[0][1]
            ),
            (
                other.data[0][0] * self.data[1][0] + other.data[1][0] * self.data[1][1],
                other.data[0][1] * self.data[1][0] + other.data[1][1] * self.data[1][1]
            )
        ))


basis_matrix2x2 = Matrix2x2((
    (1, 0),
    (0, 1)
))
