s ="AAAA"
strings = s[0]
j =0
for i in range(1,len(s)):
    if s[j] != s[i]:
        strings = strings + s[i]
    j +=1
print abs(len(strings) - len(s))
    
