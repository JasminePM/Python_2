def quick_sort(arr):
    #handling cases with 0 or 1 items
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[-1]
        less_than_pivot = [x for x in arr[:-1] if x <= pivot]
        greater_than_pivot = [x for x in arr[:-1] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

#testing

arr = [10,7,8,9,1,6,12,16]
sorted_arr = quick_sort(arr)
print("Sorted array: ", sorted_arr)
