
#Create function for dividing
def merge_sort(arr):

    #handles cases where there's only one element in the list or no element at all
    if len(arr) <= 1:
        return arr

    #divide the list into two sections
    divide = len(arr) // 2
    left_half = arr[:divide]
    right_half = arr[divide:]

    #recursively sorted each half accordingly
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


#Create a function for merging elements
def merge(left, right):

    #create a variable to store the elements inside a list and create 2 variables to hold values
    sorted_list = []
    i = j = 0

    #compare the elements from both sides and merge them in a sorted order
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    #  If there are remaining elements left on either side then just add them
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list

#Testing

arr = ["orange", "cherry", "apple", "banana", "lion", "cat", "zebra"]

print("Current List: ", arr)

sorted_arr = merge_sort(arr)

print("Sorted List: ", sorted_arr)