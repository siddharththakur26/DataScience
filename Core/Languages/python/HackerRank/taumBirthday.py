b = 3
bc = 1
w = 3
wc = 9
z = 2
cost =0 
cost = b*bc + w*wc
#print cost
giftsConverted =0
if wc > bc:
    wc = bc
    giftsConverted = w
else:
    bc = wc
    giftsConverted = b
costTemp = b*bc + w*wc + z*giftsConverted
if cost > costTemp:
    print costTemp
else:
    print cost
