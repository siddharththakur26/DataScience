''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(arr):
    cnt=0
    for i in arr:
        if i == 1:
            cnt +=1
    return cnt
            

 # Write code here 

size = int(input())
arr=[]
for i in range(size):
    arr.append(int(input()))

print (main(arr),end='')


