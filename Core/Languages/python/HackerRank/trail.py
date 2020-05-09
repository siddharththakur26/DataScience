n = 10**7
com={0:1,1:1,2:2}
for i in range(n+1):
    if i not in com:
        com[i] = com[i-1] + com[i-2]
print(com[n])