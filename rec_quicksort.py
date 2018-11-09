import time
start_time = time.time()

def quicksort(arr):
    if len(arr) <2:
        return arr
    support = arr[0]
    less = [i for i in arr[1:] if i < support]
    greater = [i for i in arr[1:] if i > support]
    return quicksort(less) + [support] + quicksort(greater)

print(quicksort([3, 5, 7, 2, 0, 1, 6, 4]))
print(time.time() - start_time)