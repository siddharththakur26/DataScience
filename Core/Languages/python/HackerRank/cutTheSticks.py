arr = [5, 4, 4, 2, 2, 8]
temp = []
length = []
while(len(arr)!= 0):
    minValue = min(arr)
    length.append(len(arr))
    for i in arr:
        element = i - minValue
        if element !=0:
            temp.append(element)
    arr = temp
    temp=[]

for i in length:
    print length
        



