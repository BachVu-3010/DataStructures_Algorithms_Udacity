def rotated_array_search(input_list, number):

    min, max = 0, len(input_list) - 1

    while min + 1 < max:
        if input_list[min] == number:
            return min

        elif input_list[max] == number:
            return max

        else:
            guess = (min + max) // 2
            if input_list[guess] == number:
                return guess

            elif input_list[guess] >= input_list[min]:
                if input_list[min] < number and number < input_list[guess]:
                    return binary_search(input_list, min, guess, number)

                else:
                    min = guess

            elif input_list[guess] < input_list[min]:
                if input_list[guess] < number and number < input_list[max]:
                    return binary_search(input_list, guess, max, number)

                else:
                    max = guess

    return -1

    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """


# Define a conventional binary search for a sorted array
def binary_search(list, min, max, number):

    if list[min] == number:
        return min
    elif list[max] == number:
        return max
    elif min + 1 >= max:
        return -1
    else:
        guess = (min + max) // 2

    if list[guess] == number:
        return guess

    if list[guess] > number:
        return binary_search(list, min, guess, number)
    else:
        return binary_search(list, guess, max, number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
