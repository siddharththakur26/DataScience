n = 352926151
m = 380324688
s = 94730870

# ans = 49690850
sweetLeft = m%n
print sweetLeft    
offset = s - 1
print offset
#prisoner = sweetLeft + offset
prisoner = (m + offset)% n
if prisoner == 0:
    print n
else:
    print prisoner

'''
n: an integer, the number of prisoners
m: an integer, the number of sweets
s: an integer, the chair number to begin passing out sweets from


prisoner =s
sweetTaken =1
while(sweetTaken < m ):
    if prisoner == n :
        prisoner = 1
    else:
        prisoner = prisoner + 1
    sweetTaken +=1
    
print prisoner
'''
