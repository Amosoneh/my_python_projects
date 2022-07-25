import doctest


def add(a, b):
    """
    >>> add(3, 5)
    0
    """
    return a + b


if __name__ == '__main__':
    doctest.testmod()
