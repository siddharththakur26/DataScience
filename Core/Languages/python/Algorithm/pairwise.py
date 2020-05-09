'''
Algorithms: Pairwise
Given an array arr, find element pairs whose sum equal the second argument arg and return the sum of their indices.

You may use multiple pairs that have the same numeric elements but different indices. Each pair should use the lowest possible available indices. Once an element has been used it cannot be reused to pair with another element. For instance, pairwise([1, 1, 2], 3) creates a pair [2, 1] using the 1 at index 0 rather than the 1 at index 1, because 0+2 < 1+2.

For example pairwise([7, 9, 11, 13, 15], 20) returns 6. The pairs that sum to 20 are [7, 13] and [9, 11]. We can then write out the array with their indices and values.

Index	0	1	2	3	4
Value	7	9	11	13	15
Below we'll take their corresponding indices and add them.

7 + 13 = 20 → Indices 0 + 3 = 3
9 + 11 = 20 → Indices 1 + 2 = 3
3 + 3 = 6 → Return 6
'''

arr=[1, 3, 2, 4]
Sum = 4
result=0
ar_val=[]
ar_index=[]
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        temp = [arr[i],arr[j]]
        ar_val.append(temp)
        ar_index.append([i,j])

temp = []
for index,val in enumerate(ar_val):
    a = ar_index[index]
    if sum(val)==Sum and ar_index[index][0] not in temp and ar_index[index][1] not in temp:
        temp.append(ar_index[index][0])
        temp.append(ar_index[index][1])
        result = result + sum(ar_index[index])

print(result)

