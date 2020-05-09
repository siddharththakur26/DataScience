'''
Algorithms: Implement Bubble Sort
This is the first of several challenges on sorting algorithms. Given an array of unsorted items, we want to be able to return a sorted array. We will see several different methods to do this and learn some tradeoffs between these different approaches. While most modern languages have built-in sorting methods for operations like this, 
it is still important to understand some of the common basic approaches and learn how they can be implemented.

Here we will see bubble sort. The bubble sort method starts at the beginning of an unsorted array and 'bubbles up' 
unsorted values towards the end, iterating through the array until it is completely sorted. It does this by comparing adjacent items and swapping them if they are out of order. The method continues looping through the array until no swaps occur at which point the array is sorted.
'''

input_arr = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
flag_swap = True
flag= True
while(flag == True):
    flag_swap=False
    for i in range(len(input_arr)-1):
        if input_arr[i] > input_arr[i+1]:
            temp = input_arr[i]
            input_arr[i] = input_arr[i+1]
            input_arr[i+1] = temp
            flag_swap = True
    
    if flag_swap == False:
        flag=False

    
print(input_arr)