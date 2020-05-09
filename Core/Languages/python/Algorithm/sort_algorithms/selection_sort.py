'''
                    Algorithms: Implement Selection Sort

Here we will implement selection sort. Selection sort works by selecting 
the minimum value in a list and swapping it with the first value in the list. 
It then starts at the second position, selects the smallest value in the remaining list, 
and swaps it with the second element. It continues iterating through the list 
and swapping elements until it reaches the end of the list. Now the list is sorted. 
Selection sort has quadratic time complexity in all cases.

'''

arr=[1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]
def find_min_value(arr,index):
    min_value =2147483647
    min_value_index=0
    k=index
    for z in arr:
        if z < min_value:
            min_value = z
            min_value_index = k
        k+=1    
    return min_value,min_value_index

def sort(arr):
    index=0
    for i in arr:
        min_value,min_value_index = find_min_value(arr[index:],index)
        temp = arr[index]
        arr[index] = min_value
        arr[min_value_index] = temp
        index+=1
    return arr

print(sort(arr))
    

    

