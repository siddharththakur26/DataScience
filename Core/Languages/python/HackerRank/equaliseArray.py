arr = [3, 3 ,2 ,1 ,3]
counts ={}
for i in set(arr):
    number = arr.count(i)
    counts[i] = number

maxValue = max(counts)
print counts
length=[]
sum=0
for i in counts:
    for j in counts:
        if i != j:
            sum = sum + counts.get(j)
    length.append(sum)
    sum=0

print min(length)        

    