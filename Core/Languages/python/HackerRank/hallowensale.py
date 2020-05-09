p = 20
d = 3
m = 6
s = 80
sum =0 
count=0
while(sum <= s):
    sum += p
    if p > m:
        p -= d
    else:
        p = m
    count+=1
print(count)