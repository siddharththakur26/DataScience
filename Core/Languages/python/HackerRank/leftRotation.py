ar=[1,2,3,4,5]
n=5
d=26
d=d%n
result=[]
for i in range(d,n):
    result.append(ar[i])

for i in range(0,d):
    result.append(ar[i])
string=""
print(' '.join(map(str,result)))