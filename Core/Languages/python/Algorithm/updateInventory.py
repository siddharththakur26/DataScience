curInv = [
    [21, "Bowling Ball"],
    [2, "Dirty Sock"],
    [1, "Hair Pin"],
    [5, "Microphone"]
]
newInv = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]

temp_inv_cur={}

for i in range(len(newInv)):
    temp_inv_cur[newInv[i][1]] = newInv[i][0]

for i in range(len(curInv)):
    print(curInv[i][1])
    if curInv[i][1] in temp_inv_cur:
        temp_inv_cur[curInv[i][1]] = curInv[i][0] + temp_inv_cur[curInv[i][1]]
    else:
        temp_inv_cur[curInv[i][1]] = curInv[i][0]

result=[]
for i in sorted(temp_inv_cur):
    e2 = i
    e1 = temp_inv_cur[i]
    temp = [e1,e2]
    result.append(temp)
print(result)



    


