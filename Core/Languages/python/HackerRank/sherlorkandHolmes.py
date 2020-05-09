import math
a = 3
b = 9
maxValue = int(round(math.sqrt(b)))
minValue = int(round(math.sqrt(a)))
cnt =0
for i in range(minValue,maxValue+1,1):
    square = i*i
    if square >=a and square <=b:
        cnt+=1
print cnt