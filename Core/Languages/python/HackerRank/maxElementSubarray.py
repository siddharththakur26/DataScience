arr = [9, 7, 2, 4, 6, 8, 2, 1, 5]
K = 3
subtemp = []
for i  in  range(0,len(arr)):
    if (i+K) <= len(arr):
        temp=[]
        temp = arr[i : i+K]
        maxxElement = max(temp)
        subtemp.append(maxxElement)
print subtemp
