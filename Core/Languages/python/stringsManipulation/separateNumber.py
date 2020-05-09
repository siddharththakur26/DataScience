s = "1"
j=1
flag=0
iterate = True
while(j < len(s) and iterate):
    number = int(s[0:j])
    smallNumber = number
    k=j
    flag =0
    while(k < len(s)):
        expectedNextNumber = number + 1
        length = len(str(expectedNextNumber))
        actualNextNumber = int(s[k:k+length])
        if expectedNextNumber == actualNextNumber:
            number = actualNextNumber
        else:
            flag +=1
        k +=length 
    if flag == 0:
        minValue = smallNumber
        iterate = False
    j +=1
if flag >0 or len(s)<=1:
    print "No"
else:
    print "Yes"+" "+str(minValue)
    





