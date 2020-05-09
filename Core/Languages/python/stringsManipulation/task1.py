# 
'''
from difflib import get_close_matches 

Above library to match the string matches closely to list of strings
'''

'''
A = "Geeks for Geeks" 
B = "Learning from Geeks for Geeks"
iA = A.split(' ')
iB = B.split(' ')
count={}
for i in iA:
    count[i] = count.get(i,0) + 1

for i in iB:
    count[i] = count.get(i,0) + 1
print count 

for i in count:
    if count[i] == 1:
        print i

'''
string = "14, 625, 498.002"
listt  = string.split(', ')
for i in range(len(listt)):
    if '.' in listt[i]:
        temp = listt[i]
        temp = temp.replace('.',', ')
        listt[i] = temp
print '.'.join(listt)
        