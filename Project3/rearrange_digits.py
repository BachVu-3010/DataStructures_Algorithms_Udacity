# Define a merge_sort function

def merge_sort(arr):

    values = []
    if len(arr) > 1:

        mid = (0 + len(arr)) // 2

        left = arr[:mid]
        right = arr[mid:]

        left = merge_sort(left)
        right = merge_sort(right)

        while len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                values.append(left[0])
                left.pop(0)
            elif left[0] > right[0]:
                values.append(right[0])
                right.pop(0)

        if len(left) > 0:
            for i in left:
                values.append(i)
        else:
            for i in right:
                values.append(i)

    if len(arr) == 1:
        values = arr
        return values

    return values


def rearrange_digits(input_list):

    sorted_input_list = merge_sort(input_list)

    ans = []
    list_length = len(sorted_input_list)
    ans1 = ""
    ans2 = ""
    if list_length % 2 == 0:
        for i in range(list_length-1, 0, -2):
            ans1 += str(sorted_input_list[i])

        for i in range(list_length-2, -1, -2):
            ans2 += str(sorted_input_list[i])

        ans1 = int(ans1)
        ans2 = int(ans2)

        ans.append(ans1)
        ans.append(ans2)

    else:
        for i in range(list_length-1, -1, -2):
            ans1 += str(sorted_input_list[i])

        for i in range(list_length-2, 0, -2):
            ans2 += str(sorted_input_list[i])

        ans1 = int(ans1)
        ans2 = int(ans2)

        ans.append(ans1)
        ans.append(ans2)

    return ans


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]

    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
