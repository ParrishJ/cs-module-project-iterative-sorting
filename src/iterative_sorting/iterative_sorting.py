import random

test_range = 10000
test_size = 10000

test_arr = random.sample(range(test_range), test_size)
new_arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
#print(test_arr)


# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    
    curr_index = 0
    smallest_index = 0

    while curr_index < len(arr): 
        for i in range(curr_index, len(arr) - 1):
            temp_curr = None
            temp_smallest = None
            
            if arr[smallest_index] > arr[i + 1]:
                smallest_index = i + 1

        if arr[curr_index] != arr[smallest_index]:
            temp_curr = arr[curr_index]
            temp_smallest = arr[smallest_index]

            arr[curr_index] = temp_smallest
            arr[smallest_index] = temp_curr
            
        curr_index += 1
        smallest_index = curr_index

    return arr


""" def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        curr_index = i
        smallest_index = curr_index
        
        for j in range(curr_index, len(arr) - 1):
            if arr[smallest_index] > arr[j + 1]:
                smallest_index = j + 1
                
        if arr[curr_index] != arr[smallest_index]:
            temp_curr = arr[curr_index]
            temp_smallest = arr[smallest_index]

            arr[curr_index] = temp_smallest
            arr[smallest_index] = temp_curr

    return arr """ 
                

    


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

    sorted_arr = list()
    error_str = "Error, negative numbers not allowed in Count Sort"

    if arr == []:
        return sorted_arr
    
    else:
        instance_list = list()
        max_value = max(arr)

        """ for _ in range(0, max_value + 1):
            instance_list.append(0)
        print('instance list', instance_list) """

        #alternative way to create a list of 0s - more elegant
        instance_list = [0] * (max_value + 1)
        
        

        for value in arr:
            if value < 0:
                return error_str

            if value > -1:
                instance_list[value] = instance_list[value] + 1

        for i in range(len(instance_list)):
            if instance_list[i] == 0:
                continue
            else:
                for _ in range(instance_list[i]):
                    sorted_arr.append(i)

        return sorted_arr



