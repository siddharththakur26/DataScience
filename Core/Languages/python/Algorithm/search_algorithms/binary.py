'''
Binary Search: Search a sorted array by repeatedly dividing the search interval in half. 
Begin with an interval covering the whole array. 
If the value of the search key is less than the item in the middle of the interval, 
narrow the interval to the lower half. Otherwise narrow it to the upper half. 
Repeatedly check until the value is found or the interval is empty.
## Divide and Conquer ##
'''
arr = [2]

def search(ar,start_index,last_index,element):
    if last_index >= start_index:
        mid_index = start_index + (last_index-start_index) //2
        mid_val = ar[mid_index]

        if ar[mid_index] == element:
            return mid_index
        
        elif mid_val > element:
            return search(ar,start_index,mid_index-1,element)

        else:
            return search(ar,mid_index+1,last_index,element)
    return None

last_index = len(arr)-1
start_index = 0
element=2
print(search(arr,start_index,last_index,element))     