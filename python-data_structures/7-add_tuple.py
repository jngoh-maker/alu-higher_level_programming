#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Return a tuple containing the sum of the first two elements."""
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)

    return (a[0] + b[0], a[1] + b[1])
