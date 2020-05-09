s = "hhaacckkekraraannk"
string = "hackerrank"
cnt=0
j=0
for i in s:
    if i == string[j]:
        cnt+=1
        j+=1

if cnt == len(string):
    print "Yes"
else:
    print "No"

