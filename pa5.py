def gcd(a, b):
    """
    Calculate the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The greatest common divisor of `a` and `b`.
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def remove_pairs(s):
    """
    Recursively remove pairs of opposite directions from the given direction string.

    Args:
        s (str): A string containing directions 'N', 'S', 'E', 'W'.

    Returns:
        str: A string with opposite pairs removed.
    """
    if len(s) == 1:
        return s
    direction_dict = {"S": "N", "E": "W", "N": "S", "W": "E"}
    if len(s) > 1 and direction_dict[s[0]] == s[1]:
        if len(s) == 2:
            return ""
        return remove_pairs(s[2:])
    return s[0] + remove_pairs(s[1:])


def bisection_root(func, a, b):
    """
    Find the root of a function within a given interval using the bisection method.

    Args:
        func (callable): The function for which to find the root.
        a (float): The lower bound of the interval.
        b (float): The upper bound of the interval.
        tolerance (float): The tolerance level for finding the root (default: 1e-10).

    Returns:
        float: The root of `func` within the interval.

    Raises:
        ValueError: If the signs of the function at the interval boundaries are not different.
    """
    if func(a) > 0 and func(b) < 0:
        lower = b
        upper = a
    elif func(a) < 0 and func(b) > 0:
        lower = a
        upper = b
    else:
        raise ValueError

    if abs(func(lower)) < 1e-10:
        return lower
    elif abs(func(upper)) < 1e-10:
        return upper

    midway = (lower + upper) / 2
    mid = func(midway)
    if mid > 0:
        return bisection_root(func, lower, midway)
    elif mid < 0:
        return bisection_root(func, midway, upper)
    return midway
