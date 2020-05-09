# m
decimalNumber = 5
# n
n = 3
# k
k = 3
def conversionToBinary(decimalNumber):
    return bin(decimalNumber).replace("0b","")

binaryNumber = conversionToBinary(decimalNumber)
sn =""
sn = binaryNumber
newStr=""
for i in range(0,n):
    for j in range(0,len(sn)):
        if sn[j] == "0":
            newStr = newStr + "01"
        else :
            newStr = newStr + "10"
    sn = newStr
    newStr=""
print(sn[k])