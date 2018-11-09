def rec_binary_search(arr, num):
    mid = int(len(arr)/2)
    if arr[mid] == num:
        return arr[mid]
    return rec_binary_search(arr[:mid-1], num) if arr[mid] > num else rec_binary_search(arr[mid +1:], num)

arr = [1, 2, 3, 4, 5, 6, 7, 8]
print(rec_binary_search(arr, 7))