from vector import Vector2d, i_2d_vector, j_2d_vector


class LinearCombination2d:
    """
    A linear combination with its own span

    Parameters
    ----------
    a : Vector2d
        First vector
    b : Vector2d
        Second vector

    Methods
    -------
    span()
        Returns span.
        Span displays in which dimension the resulting vector can be. 0 — 0D, point. 1 — 1D, line. 2 — 2D, plane
    """

    def __init__(self, a: Vector2d, b: Vector2d):
        self.a = a
        self.b = b
        self.vector = a + b
        if self.a.coords == (0, 0) and self.b.coords == (0, 0):
            self._span = 0
        else:
            a_ratio = 'zero_division' if self.a.coords[1] == 0 else self.a.coords[0] / self.a.coords[1]
            b_ratio = 'zero_division' if self.b.coords[1] == 0 else self.b.coords[0] / self.b.coords[1]
            if self.a.coords == (0, 0) or self.b.coords == (0, 0) or a_ratio == b_ratio:
                self._span = 1
            else:
                self._span = 2

    @property
    def span(self):
        """
        Returns span.
        Span displays in which dimension the resulting vector can be. 0 — 0D, point. 1 — 1D, line. 2 — 2D, plane

        Returns
        -------
        int
        """
        return self._span


basis_2d_linear_combination = LinearCombination2d(i_2d_vector, j_2d_vector)
