'''
The Interpolation Search 

interpolation search may go to different locations according to the value of the 
key being searched. For example, if the value of the key is closer to the last element, 
interpolation search is likely to start search toward the end side.
'''

arr = [10, 12, 13, 16, 18, 19, 20, 21,22, 23, 24, 33, 35, 42, 47] 
size = len(arr)
element = 20
def search(arr,size,element):
    start_index = 0
    last_index = size-1

    while last_index>=start_index and element>=arr[start_index] and element<=arr[last_index]:
        if start_index == last_index:
            if arr[start_index] == element:
                return start_index
            return None
        
        position = int(start_index + ((element - arr[start_index]) * (last_index-start_index) / (arr[last_index]-arr[start_index])))
        
        if arr[position] == element:
            return position
        
        if arr[position] < element:
            start_index +=1
        else:
            last_index -=1
        
    return None

print(search(arr,size,element))
    

    
