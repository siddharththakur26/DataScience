a = [3,4,5]
k = 1
queries = [1,2]
out=[]
rotate = k

def rotation(rotate, a):
    index = len(a) - rotate
    lastSubarray = a[index:]
    firstSubarray = a[:index]
    for i in lastSubarray:
        out.append(i)
    for i in firstSubarray:
        out.append(i)
    

if rotate == len(a):
    out = a
elif rotate > len(a):
    rotate = k % len(a)
    rotation(rotate, a)
else:
    rotation(rotate,a)
result =[]
print out
for i in queries:
    result.append(out[i])
print result





  

'''
a = [3,4,5]
k = 2
queries = [1,2]
rotation = 1

while rotation <= k:
    out=[]
    out.append(a[len(a)-1])
    #out.append(a[0:len(a)-1])
    for i in range(0,len(a)-1):
        out.append(a[i])
    a = out
    rotation = rotation + 1
result=[]
for i in queries:
    result.append(out[i])
    
'''

        


