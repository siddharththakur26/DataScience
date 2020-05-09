'''
A simple approach is to do linear search, i.e
Start from the leftmost element of arr[] 
and one by one compare x with each element of arr[]
If x matches with an element, return the index.
'''

input_arr = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92]

def search(arr,element):
    '''
    if element in arr:
        return True
    return False
    '''
    for i in arr:
        if element == i:
            return True
    
    return False

print(search(input_arr,2))