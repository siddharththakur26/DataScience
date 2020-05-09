'''
                        Algorithms: Implement Insertion Sort

The next sorting method we'll look at is insertion sort. 
This method works by building up a sorted array at the beginning of the list.
It begins the sorted array with the first element. Then it inspects the next element 
and swaps it backwards into the sorted array until it is in sorted position. 
It continues iterating through the list and swapping new items backwards into the 
sorted portion until it reaches the end. 
This algorithm has quadratic time complexity in the average and worst cases.
'''

arr=[1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
#arr=[7,8,5,2,4,6,3]
def sort_sub_array(ar,index):
    if index==0:
        return ar 
    elif ar[index-1] > ar[index]:
            temp = ar[index-1]
            ar[index-1] = ar[index]
            ar[index] = temp
    return sort_sub_array(ar,index-1)
    

def sort(arr):
    for i in range(1,len(arr)):
        sub_arr = arr[:i+1]
        index = len(sub_arr)-1
        temp_arr = sort_sub_array(sub_arr,index)
        arr = temp_arr + arr[i+1:]
        
    return arr

print(sort(arr))




        
