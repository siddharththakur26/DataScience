s = "banana"
cnt =0
flag = 0
start =0
while(flag != -1):
    flag = s.find('ana',start)
    if flag != -1:
        cnt +=1
    start = flag + len('ana')-1
print cnt    

