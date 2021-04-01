def min_max(l):
    """
    >>> min_max([1,2,3])
    (1, 3)

    >>> min_max([2,5,0])
    (0, 5)

    >>> min_max([-1, 5, 0])
    (-1, 5)

    :return:
    """
    return _min_max(l)


def _min_max(l, pos=-0, min=float('inf'), max=float('-inf')):
    x = l[pos]

    if x < min:
        min = x
    elif x > max:
        max = x

    if pos+1 == len(l):
        return min, max

    return _min_max(l, pos+1, min, max)

