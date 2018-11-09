def count_list(arr):
    if arr == []:
        return 0
    return 1 + count_list(arr[1:])

print(count_list([15, 's', 'dg']))