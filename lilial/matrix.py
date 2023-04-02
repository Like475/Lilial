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
    determinant
        Returns determinant
    data
        Returns data
    """

    def __init__(self, data: (tuple, list)):
        self._data = (
            (data[0][0], data[0][1]),
            (data[1][0], data[1][1])
        )
        self._determinant = self._data[0][0] * self._data[1][1] - self._data[1][0] * self._data[0][1]

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
                other._data[0][0] * self._data[0][0] + other._data[1][0] * self._data[0][1],
                other._data[0][1] * self._data[0][0] + other._data[1][1] * self._data[0][1]
            ),
            (
                other._data[0][0] * self._data[1][0] + other._data[1][0] * self._data[1][1],
                other._data[0][1] * self._data[1][0] + other._data[1][1] * self._data[1][1]
            )
        ))

    @property
    def data(self) -> tuple:
        """
        Returns data

        Returns
        -------
        tuple
        """
        return self._data

    @property
    def determinant(self) -> int:
        """
        Returns determinant

        Returns
        -------
        int
        """
        return self._determinant


basis_matrix2x2 = Matrix2x2((
    (1, 0),
    (0, 1)
))
