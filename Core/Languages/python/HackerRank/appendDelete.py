s = "aba"
t = "aba"
k = 7
spad = s
tpad = t
if len(s) < len(t):
    j = len(s)
    while(j < len(t)):
        spad = spad + "0"
        j+=1
elif len(s) > len(t):
    j = len(t)
    while(j < len(s)):
        tpad = tpad + "0"
        j+=1
print spad
print tpad
FirstIndexToRemove = 0
flag =0
for i in range(0,len(spad)):
    j = i 
    if spad[i] != tpad[j]:
        FirstIndexToRemove = i
        flag +=1
        break
            
print FirstIndexToRemove
numberOfOperations = 0
output =""
if flag !=0:
    characterToRemove = len(s) - FirstIndexToRemove 
    print characterToRemove   
    characterToFill = len(t) - FirstIndexToRemove
    print characterToFill    
    numberOfOperations = characterToFill + characterToRemove
    print numberOfOperations

OperationLeft = k - numberOfOperations



if numberOfOperations !=k and FirstIndexToRemove != 1 and numberOfOperations !=0: 
    if OperationLeft > 0 and OperationLeft%2 !=0:
        print "No"
    elif numberOfOperations > k:
        print "No"
    else:
        print "Yes"
elif abs(len(t)-k) > len(t):
    print "Yes"
else:
    print "Yes"





'''
charArrayS = [0]*26
for i in s:
    charArrayS[ord(i)-97] = charArrayS[ord(i)-97] + 1 
print charArrayS
charArrayT = [0]*26
for i in t:
    charArrayT[ord(i)-97] = charArrayT[ord(i)-97] + 1 
print charArrayT

numberOfOperation = 0
cnt =0
for i in range(0,26):
    numberOfOperation =  (charArrayT[i]-charArrayS[i])
    if numberOfOperation < 0:
        cnt = cnt - numberOfOperation
    elif charArrayS[i] > 0 and numberOfOperation > 0:
        cnt +=numberOfOperation + 1
    else:
        cnt +=numberOfOperation
print cnt

if len(s) == len(t):
   if cnt == k or cnt==0:
        print "Yes"
elif cnt <= k:
    print "Yes"
else:
    print "No" 
'''