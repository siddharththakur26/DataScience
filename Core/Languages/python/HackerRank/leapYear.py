year = 2400
leap = False
if year%4==0:
    leap= True
    if year%100 == 0:
        leap = False
        if year%400 == 0:
            leap = True
    else:
        leap = False
print leap

