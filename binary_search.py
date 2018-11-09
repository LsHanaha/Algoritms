def binary_search(num, min, max):
    while (min <= max):
        mid = int((min + max)/2)
        if num > mid:
            min = mid + 1
        if num < mid:
            max = mid - 1
        print(mid)
        if num == mid:
            print("your number = ", mid)
            return mid
    return None


binary_search(7, 0, 100)


