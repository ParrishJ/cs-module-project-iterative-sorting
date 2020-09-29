test_arr = [2, 4, 1, 3, 5, 88, 17, 23, 54, 67]

# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    
    curr_index = 0
    smallest_index = 0

    while curr_index < len(arr):
        print('curr index', curr_index)
        print('smallest index', smallest_index)
        print('arr at beginning of loop', arr) 
        for i in range(curr_index, len(arr) - 1):
            print('i', i)
            temp_curr = None
            temp_smallest = None
            #cur_index = i
            
            # TO-DO: find next smallest element
            # (hint, can do in 3 loc)
            # Your code here
            
            if arr[smallest_index] > arr[i + 1]:
                smallest_index = i + 1

        if arr[curr_index] != arr[smallest_index]:
            temp_curr = arr[curr_index]
            temp_smallest = arr[smallest_index]

            arr[curr_index] = temp_smallest
            arr[smallest_index] = temp_curr
            
        curr_index += 1
        smallest_index = curr_index

        print('arr at end of loop', arr)


            # TO-DO: swap
            # Your code here
    print(arr)
    return arr

selection_sort(test_arr)

# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    sort_continue = True
    swaps = 0
    while sort_continue == True:
        for element in range(len(arr) - 1):
            
            temp_left = None
            temp_right = None

            if arr[element + 1] < arr[element]:
                temp_left = arr[element]
                temp_right = arr[element + 1]

                arr[element + 1] = temp_left
                arr[element] = temp_right

                swaps += 1
               
            
        if swaps > 0:
            sort_continue = True
            swaps = 0
        else:
            sort_continue = False
        
    return arr
    





    #return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
