import operator
arr = [2,2,1,3,1,2] 
tempArr = sorted(arr)
print tempArr

birdTypes = set([])
for i in tempArr:
    birdTypes.add(i)

print birdTypes
cnt = 0
d={}
for i in birdTypes:
    cnt = arr.count(i)
    d[i] = cnt

print d
print max(d.iteritems(), key=operator.itemgetter(1))[0]

