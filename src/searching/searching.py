def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


   


# Write an iterative implementation of Binary Search

test_data = [1, 2, 3, 4, 5, 6]




def binary_search(arr, target):

    first = 0
    last = int(len(arr) - 1)
    middle_index = 0
    

    while(first <= last):

        middle_index = (first + last) // 2
        
        if target == arr[middle_index]:
            return middle_index

        if target < arr[middle_index]:
            last = middle_index - 1
        
        else:
            first = middle_index + 1
        
    return -1  # not found

