'''
Create a function that takes two or more arrays and returns an array of the symmetric 
difference (△ or ⊕) of the provided arrays.

Given two sets (for example set A = {1, 2, 3} and set B = {2, 3, 4}), the mathematical term 
"symmetric difference" of two sets is the set of elements which are in either of the two sets, 
but not in both (A △ B = C = {1, 4}).

For every additional symmetric difference you take (say on a set D = {2, 3}), you should get the set with elements which are in either of the two the sets but not both (C △ D = {1, 4} △ {2, 3} = {1, 2, 3, 4}). The resulting array must contain only unique values (no duplicates).
'''
arr = [[1, 2, 3], [5, 2, 1, 4, 5]]
#arr=[[1, 2, 3], [5, 2, 1, 4]]
list1=list2=result=[]
def sd_array(a,b):
    num = set()
    for k in a:
        if k not in b:
            num.add(k)
    for k in b:
        if k not in a:
            num.add(k)

    return num

for i in range(0,len(arr)-1):
    if i != len(arr)-1 and len(result) == 0:
        list1=arr[i]
        list2=arr[i+1]
    else:
        list1 = result
        list2=arr[i+1]
   
    
    result = sd_array(list1,list2)
print(result)  
