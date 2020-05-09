var ="geeksgeeks"
char = [0] * 256
#print char[0]
for i in range(0,len(var)):    
    char[ord(var[i])-ord('a')] = char[ord(var[i])-ord('a')] + 1
#print char
cnt=0
for i in char:
    if i % 2 != 0 :
        cnt = cnt +1
        break

if cnt > 0:
    print "Not Pallindrome"
else:
    print "Pallindrome"
