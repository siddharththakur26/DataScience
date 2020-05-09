A = [-2, 1, 3, 6, 5,4, 2] 
A.sort()
num =  A[len(A)-1]
missingNumber = 0
for i in range(1,num):
    if i not in A:
        missingNumber = i
        break
#print index

if num > 0 :
    if missingNumber != 0:
        print missingNumber
    else:
        print num+1
else :
    print 1



