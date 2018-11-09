def selection_sort(unsort_array):
    sort_array = []
    while len(unsort_array) > 0:
        i = 0
        min = unsort_array[0]
        while i < len(unsort_array):
            if unsort_array[i] < min:
                min = unsort_array[i]
            i+=1
        sort_array.append(min)
        unsort_array.remove(min)    
    return sort_array

print(selection_sort([1, 8, 6, 4, 15]))