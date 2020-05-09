ar = [13,26,17]
sorted(ar)
print ar
cnt = 0 



def reducee(ar,cnt):
    temp =[]
    if not ar:   
        return cnt
    divsor = ar[0]
    for i in ar:
        if i % divsor != 0 :
            temp.append(i)
    cnt = cnt + 1        
    return reducee(temp,cnt)


print reducee(ar,cnt)