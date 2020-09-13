import random


def get_min_max(ints):

    if not ints:
        return None

    min, max = ints[0], ints[0]

    for i in range(len(ints)):
        if ints[i] < min:
            min = ints[i]

        if ints[i] > max:
            max = ints[i]

    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    return (min, max)


l = []  # An empty list
print("Pass:\nList: " + str(l) + "\n(min, max): " +
      str(get_min_max(l)) if (None is get_min_max(l)) else "Fail")
print()

l = [1]  # An list with one element
print("Pass:\nList: " + str(l) + "\n(min, max): " +
      str(get_min_max(l)) if ((1, 1) == get_min_max(l)) else "Fail")
print()

l = [i for i in range(0, 10)]  # A list containing 0 to 9
random.shuffle(l)
print("Pass:\nList: " + str(l) + "\n(min, max): " +
      str(get_min_max(l)) if ((0, 9) == get_min_max(l)) else "Fail")
print()

l = [i for i in range(-12, 25)]  # a list containing -12 to 24
random.shuffle(l)
print("Pass:\nList: " + str(l) + "\n(min, max): " +
      str(get_min_max(l)) if ((-12, 24) == get_min_max(l)) else "Fail")
print()

l = [i for i in range(-24, -1)]  # a list containing -24 to -2
random.shuffle(l)
print("Pass:\nList: " + str(l) + "\n(min, max): " +
      str(get_min_max(l)) if ((-24, -2) == get_min_max(l)) else "Fail")
print()
