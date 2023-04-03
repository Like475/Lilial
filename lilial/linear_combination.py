from .vector import Vector2d, i_2d_vector, j_2d_vector


class LinearCombination2d:
    """
    Linear combination with its own span

    Parameters
    ----------
    a : Vector2d
        First vector
    b : Vector2d
        Second vector

    Methods
    -------
    a
        Returns first vector
    b
        Returns second vector
    vector
        returns a + b vector
    span
        Returns span.
        Span displays in which dimension the resulting vector can be. 0 — 0D, point. 1 — 1D, line. 2 — 2D, plane
    """

    def __init__(self, a: Vector2d, b: Vector2d):
        self._a = a
        self._b = b
        self._vector = a + b
        if self._a.coords == (0, 0) and self._b.coords == (0, 0):
            self._span = 0
        else:
            a_ratio = 'zero_division' if self._a.coords[1] == 0 else self._a.coords[0] / self._a.coords[1]
            b_ratio = 'zero_division' if self._b.coords[1] == 0 else self._b.coords[0] / self._b.coords[1]
            if self._a.coords == (0, 0) or self._b.coords == (0, 0) or a_ratio == b_ratio:
                self._span = 1
            else:
                self._span = 2

    @property
    def a(self) -> Vector2d:
        """
        Returns first vector

        Returns
        -------
        Vector2d
        """
        return self._a

    @property
    def b(self) -> Vector2d:
        """
        Returns second vector

        Returns
        -------
        Vector2d
        """
        return self._b

    @property
    def vector(self) -> Vector2d:
        """
        Returns a + b vector

        Returns
        -------
        Vector2d
        """
        return self._vector

    @property
    def span(self) -> int:
        """
        Returns span.
        Span displays in which dimension the resulting vector can be. 0 — 0D, point. 1 — 1D, line. 2 — 2D, plane

        Returns
        -------
        int
        """
        return self._span


basis_2d_linear_combination = LinearCombination2d(i_2d_vector, j_2d_vector)
