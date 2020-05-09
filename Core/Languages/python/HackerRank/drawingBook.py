n = 4
p = 4
pagesTurned=0
pagesTurnedFromFront=0
pagesTurnedFromBack=0
for i in range(2,n):
    if i%2 == 0 and i <= p:
        pagesTurnedFromFront +=1

for i in range(n-1,2,-1):
   if i%2 != 0 and i >= p:
        pagesTurnedFromBack +=1

print min(pagesTurnedFromFront,pagesTurnedFromBack)

'''
if p <= 1 or p == n:
    pagesTurned=0
elif (n%2 !=0) and (p>= n-2 or p>= n-1):
    pagesTurned=0
# when p is even
elif (p+1)%2 != 0:
    pagesTurned = (p+1)%2
# when p is odd
elif p%2 != 0:
    pagesTurned = 1
    while(pagesTurned != p):
        pagesTurned += 2


print pagesTurned
'''



