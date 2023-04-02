class Matrix2x2:
    """
    Matrix 2 by 2

    Parameters
    ----------
    data : tuple or list
        Matrix data

    Methods
    -------
    multiply(other)
        Multiplies the matrix received at the input by this
    """
    def __init__(self, data: (tuple, list)):
        self.data = (
            (data[0][0], data[0][1]),
            (data[1][0], data[1][1])
        )

    def multiply(self, other):
        """
        Multiplies the matrix received at the input by this

        Parameters
        ----------
        other : Matrix2x2
            The matrix M1 in the formula 'M1 * M2 = M3',
            where M2 is the given matrix, and M3 is the result of multiplying two matrices

        Returns
        -------
        Matrix2x2
        """
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
