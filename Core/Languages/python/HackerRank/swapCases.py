s = "Www.HackerRank.com"
out=""
temp=""
for i in s:
    if i.islower():
        temp = i.upper()
        out= out + temp
    elif i.isupper():
        temp = i.lower()
        out = out + temp
    else:
        out = out + i
print out