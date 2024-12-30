#Implement the bubble sort algorithm in to sort a list of numbers in ascending order

#Create a bubble sort function
def bubble_sort(arr):

    #store the length of your list(array) in a variable
    number = len(arr)

    #nested loop to go through and traverse all elements inside your list
    for i in range(number):

        #create a placeholder for swaps and assign it to False
        swapped = False

        #create a nested loop that will take elements from our first loop and check it, if it isn't sorted then we must check it and if it is we leave it
        for j in range(0, number - i - 1):

            #compare current element with the next element  and swap if in the wrong order
            if arr[j] > arr[j + 1]:

                #swap elements if in the wrong order
                arr[j], arr[j +1] = arr[j + 1], arr[j]

                swapped = True
        #if no swapping occurs, then the list is sorted
        if not swapped:
            break

    return arr

#Testing
arr = [64,34,25,12,22,11,90]

print("Current List:", arr)

sorted_arr = bubble_sort(arr)

print("Sorted List:", sorted_arr)