def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def remove_pairs(s):
    if len(s) == 1:
        return s
    direction_dict = {"S": "N", "E": "W", "N": "S", "W": "E"}
    if len(s) > 1 and direction_dict[s[0]] == s[1]:
        if len(s) == 2:
            return ""
        return remove_pairs(s[2:])
    return s[0] + remove_pairs(s[1:])


def bisection_root(func, a, b):
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
