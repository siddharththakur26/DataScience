n =int(input())
length = len(str(n))
arr= []
for i in range(1,n+1):
    temp = str(i)
    temp_length= len(temp)
    temp_space = temp.rjust((length-temp_length+1))
    arr.append(temp_space)

for i in range(len(arr)):
    for j in range(n):
        if j != len(arr)-1:
            print(arr[i],end=' ')
        else:
            if j == n-1 and arr[i] == str(n):
                print(arr[i],end='')
            else:
                print(arr[i])
