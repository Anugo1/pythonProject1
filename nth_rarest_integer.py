# Python 3 program to find the nth rarest item.


def nth_most_rate_signature(arr, n):
    # Sort the array
    arr.sort()

    # find the min frequency using
    # linear traversal
    min_count = n + 1
    res = -1
    curr_count = 1
    for i in range(1, n):
        if (arr[i] == arr[i - 1]):
            curr_count = curr_count + 1
        else:
            if (curr_count<min_count):
                min_count = curr_count
                res = arr[i - 1]

            curr_count = 1

    # If last element is least frequent
    if (curr_count < min_count):
        min_count = curr_count
        res = arr[n - 1]

    return res


# Driver program
arr = [1, 3, 2, 3, 1, 4, 3, 2, 2, 3, 1]
n = len(arr)
print("", nth_most_rate_signature(arr, n), "is the rarest nth item")

