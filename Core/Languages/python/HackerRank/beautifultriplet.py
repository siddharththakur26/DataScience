d = 1
arr =[1]
triplet=[]
result=0
arr = sorted(arr)

for i in arr:
    first_element = i
    triplet.append(first_element)
    second_element = first_element + d
    if second_element in arr:
        triplet.append(second_element)
    third_element = second_element + d
    if third_element in arr:
        triplet.append(third_element)
    if len(triplet) == 3:
        result +=1
    triplet=[]
print(result)
