import re
from itertools import permutations
A= 1
B = 2
C = 3
D = 8

time = permutations([A,B,C,D])
storeTime = set([])
for i in time:
    tenHourTime = i[0]
    unitHourTime = i[1]
    tenMinTime  =  i[2]
    unitMinTime =  i[3]
    timeFormat = `tenHourTime` + `unitHourTime` +':'+ `tenMinTime` + `unitMinTime`
    storeTime.add(timeFormat)
#print storeTime
cnt = 0
regexp = re.compile("(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])")
saveTime = []
for i in storeTime:
    #print i
    while regexp.search(i):
        saveTime.append(i)
        cnt = cnt +1
        break

print sorted(saveTime)
print cnt
'''
map = [A,B,C,D]
storeTime = []
tensHourTime=[]
for i  in [0,1,2]:
    if i in map:
        tensHourTime.append(i)   
#print tensHourTime
unitHourTime=[]
for i  in [0,1,2,3,4,5,6,7,8,9]:
    if i in map:
        unitHourTime.append(i)  

#print unitHourTime 

tensMinTime=[]
for i  in [0,1,2,3,4,5]:
    if i in map:
        tensMinTime.append(i)  
#print tensMinTime

unitMinTime=[]
for i  in [0,1,2,3,4,5,6,7,8,9]:
    if i in map:
        unitMinTime.append(i)  

#print unitMinTime
storeTime=[]
timeDigitFrequency = {A:1,B:1,C:1,D:1}
for i in tensHourTime:
    for j in unitHourTime:
        for k in tensMinTime:
            for l in unitMinTime:
                time = `i` + `j` + ':' + `k` + `l`
                storeTime.append(time)
cnt = 0
regexp = re.compile("(24:00|2[0-3]:[0-5][0-9]|[0-1][0-9]:[0-5][0-9])")
for i in storeTime:
    print i
    while regexp.search(i):
        cnt = cnt +1
        break

print cnt
'''







