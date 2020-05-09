x1 = 21 #21
v1 = 6 #6
x2 = 47 #47
v2 = 3 #3
meetingpoint =0
if v1 > v2:
    distanceBetweenKangaroos = abs(x1-x2)
    meetingpoint  = (distanceBetweenKangaroos)%abs(v2-v1)
    if meetingpoint !=0:
        print "NO"
    else:
        print "YES"
else:
    print "NO"