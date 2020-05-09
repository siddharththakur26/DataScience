'''
Find the longest substring that unique characters 
'''

word = "ABDEFGABEF"
newWordArray=[]
newWord=""
for i in range(0,len(word)):
    newWord = word[i]
    for j in range(i+1,len(word)):
        if  word[j] not in newWord:
            newWord = newWord + word[j]
        else:
            newWordArray.append(newWord)
            newWord = ""
            break

print(newWordArray)    
print(len(max(newWordArray,key=len)))

