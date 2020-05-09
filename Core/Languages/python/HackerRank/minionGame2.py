string = "BANANA"
# consonents
stuart = 0

# vowels
kevin = 0
n = len(string)
for i in range(n):
    if string[i] in ('A', 'E', 'I', 'O', 'U'):
        kevin += n - i
    else:
        stuart += n - i

if kevin > stuart:
    print 'Kevin', kevin
elif stuart > kevin:
    print 'Stuart', stuart
else:
    print 'Draw'