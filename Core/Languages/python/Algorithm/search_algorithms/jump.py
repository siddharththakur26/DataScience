'''
Jump Search is a searching algorithm for sorted arrays. 
The basic idea is to check fewer elements (than linear search) 
by jumping ahead by fixed steps or skipping some elements in place of searching all elements.
STEP 1: Jump from index 0 to index 4;
STEP 2: Jump from index 4 to index 8;
STEP 3: Jump from index 8 to index 12;
STEP 4: Since the element at index 12 is greater than 55 we will jump back a step to come to index 8.
STEP 5: Perform linear search from index 8 to get the element 55.

Time Complexity : O(√n)
'''

import math
arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,34, 55, 89, 144, 233, 377, 610 ]
element = 144
size = len(arr)

def search(arr,element,size):
    # define the number of steps to jump
    inc_step = int(math.sqrt(size))-1
    previous_index=0
    while arr[previous_index] < element:
        previous_index += inc_step
        if previous_index >=size:
            return None
    
    previous_index -= inc_step
    while arr[previous_index] < element:
        #print(arr[previous_index])
        previous_index += 1
    
    if  arr[previous_index] == element:
        return previous_index
    
    return None    




print(search(arr,element,size))
        

    




