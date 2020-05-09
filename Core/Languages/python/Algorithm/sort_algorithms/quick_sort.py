arr = [10,80,30,90,40,50,70]


def pivot_element(ar):
    return ar[len(ar)-1]

def swap(arr,i,j,pivot_element,flag):
    if arr[i] <= pivot_element:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        flag = True
        return j+1,flag
    return j,flag


def sort(arr):
    pe = pivot_element(arr)
    index_to_swap= 0
    flag = False
    for index in range(len(arr)):
        index_to_swap,flag = swap(arr,index,index_to_swap,pe,flag)
    
    
    sort(arr[:index_to_swap-1])
    sort(arr[index_to_swap:])

    
    return arr
    
       
print(sort(arr))
    
