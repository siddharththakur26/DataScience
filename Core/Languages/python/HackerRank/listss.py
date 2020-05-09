'''
input format:
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''
N = int(raw_input())
arr=[]
for i in range(N):
    line = raw_input().split()
    funcName, values = line[0], line[1:]
    if funcName == 'print':
        print arr
    elif funcName == 'sort':
        arr.sort()
    elif funcName == 'remove':
        for i in values:
            arr.remove(int(i))
    elif funcName == 'append':
        for i in values:
            arr.append(int(i))
    elif funcName == 'insert':
        arr.insert(int(values[0]),int(values[1]))   
    elif funcName == 'pop':
        arr.pop()
    elif funcName == 'reverse':
        arr.reverse()


