s = [2,5,1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
d = 18
m = 7
temp=[]
cnt=0
for i in range(0,len(s)):
    temp = s[i:m+i]
    if len(temp) == m:
        #print temp
        sumValue = sum(temp)
        #print sumValue
        if sumValue == d:
            cnt +=1
        
print cnt       
    

'''
result =[]
sum=0
cnt=0

for i in range(0,len(s)):
    j=0
    while(j < m and i+j < len(s)):
        sum = sum + s[i+j]
        if sum <= d:
            result.append(s[i+j])
            if len(result) == m:
                if sum == d:
                    cnt +=1 
        j +=1   
    del result[:] 
    sum = 0 
print cnt
'''

    

    
