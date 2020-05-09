size = 10
import string
alphabets = string.ascii_lowercase
arr =[]
for i in range(size):
    s = '-'.join(alphabets[i:size])
    temp = (s[::-1] + s[1:]).center(4*size-3,'-')
    arr.append(temp)

for i in range(len(arr)-1,-1,-1):
    print arr[i]
for i in range(1,len(arr)):
    print arr[i]
