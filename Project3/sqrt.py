import math


def sqrt(number):
    if number < 0:
        return math.nan
    if number <= 1:
        return number
    else:
        half = number // 2 + 1

        return binary_search(0, half, number)


def binary_search(min, max, ans):
    if min ** 2 == ans:
        return min
    elif max ** 2 == ans:
        return max
    else:
        guess = (min + max) // 2

        if guess ** 2 == ans or max - min <= 1:
            return guess
        elif guess ** 2 < ans:
            return binary_search(guess, max, ans)
        else:
            return binary_search(min, guess, ans)
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """


print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
