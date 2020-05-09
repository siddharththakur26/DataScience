
def calculateScore(word):
    score=0
    for i in word:
        word = i
        cnt=0
        length = len(word)
        for j in range(0,len(string)):
            wordInString = string[j:j+length] 
            if word == wordInString:
                cnt +=1
        score += cnt
    return score

def formWords(string,flag):
    vowels = ['A','E','I','O','U']
    word =set([])
    for i in range(0,len(string)):
        tempLetter = string[i]
        if flag == True:
            if tempLetter not in vowels:
                for j in range(i+1,len(string)+1):
                    tempString = string[i:j]
                    word.add(tempString)
        else:
            if tempLetter in vowels:
                for j in range(i+1,len(string)+1):
                    tempString = string[i:j]
                    word.add(tempString)
    return word


string = "BANANA"
# form words for Stuart
wordStuarts = formWords(string,True)
#print wordStuarts
scoreStuarts = calculateScore(wordStuarts)
#print scoreStuarts
wordKevins = formWords(string,False)
#print wordKevins
scoreKevins = calculateScore(wordKevins)
#print scoreKevins

if scoreStuarts > scoreKevins:
    print "Stuart "+str(scoreStuarts)
else:
    print "Kevin "+str(scoreKevins)

    
