def find_biggest(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] >= arr[1] else arr[1]
    temp_max = find_biggest(arr[1:])
    return arr[0] if temp_max<= arr[0] else temp_max

print(find_biggest([9, 2, 5, 7, 3]))
    