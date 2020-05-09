a = [1,2,2,3,1,2]
n = len(a)
a = sorted(a)
maxLength = 0
for i  in range(0,n):
    lastIndex = i
    firstValue = a[i]
    firstIndex = i
    while(lastIndex < n):
        lastValue = a[lastIndex]
        diff =lastValue - firstValue
        if diff <=1:
            lastIndex += 1 
        else:
            break
    length = len(a[firstIndex:lastIndex])
    if maxLength < length :
        maxLength = length
print maxLength

    



