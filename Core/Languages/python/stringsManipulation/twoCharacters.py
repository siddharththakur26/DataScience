s ="asdcbsdcagfsdbgdfanfghbsfdab"
arr=[]
allAlphabets = ""
for i in set(s):
    allAlphabets = allAlphabets + i
    arr.append(i)
alternateChar=[]
for i in range(0,len(arr)):
    prevChar = arr[i]
    for j in range(i+1,len(arr)):
        nextChar = arr[j]
        string=""
        string = prevChar + nextChar
        alternateChar.append(string)
#print alternateChar 
#print allAlphabets

storeValue =[]
for i in alternateChar:
    letter1 = i[0]
    letter2 = i[1]
    result=""
    result = allAlphabets.replace(letter1,"")
    result = result.replace(letter2,"")
    storeValue.append(result)

      
alternateStrings=[]
for i in storeValue:
    temp = s
    for j in range(0,len(i)):
        temp = temp.replace(i[j],"")
    alternateStrings.append(temp)
print alternateStrings

maxValue=0

for i in alternateStrings:
    flag=0
    for j in range(0,len(i)-1):
        if i[j] == i[j+1]:
            flag +=1
    if flag == 0:
        length = len(i)
        if maxValue < length:
            maxValue = length

print maxValue




