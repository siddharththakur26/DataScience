n = 8
s = "UDDU"
countStep=0
countValley =0
for move in s:
    if move == 'U':
        countStep += 1
        if countStep == 0:
            countValley +=1
    else:
        countStep -= 1
print countValley
   