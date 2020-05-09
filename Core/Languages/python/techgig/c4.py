''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def get_matrix_size():
    [m,n] = input().split(' ')
    return m,n

def get_matrix(m):
    inn = []
    for i in range(int(m)):
        inn.append(input().split(' '))    
    return inn

def main(input1,input2):
    result=[]
    for i in range(len(input1)):
        temp=[]
        for j in range(len(input2[0])):
            temp.append(int(input1[i][j]) + int(input2[i][j]))
        result.append(temp)
    return result

 # Write code here 
m1,n1 = get_matrix_size()
input1 = get_matrix(m1)
m2,n2 = get_matrix_size()
input2 = get_matrix(m2)
output = main(input1,input2)

for i in output:
    for j in i:
        print(j,end=' ')
    print(end='\n')

