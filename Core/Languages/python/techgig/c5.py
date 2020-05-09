''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main(inn):
    result=[]
    for j in range(len(inn[0])):
        temp=[]
        for i in range(len(inn)):
            temp.append(inn[i][j])
        result.append(temp)
    return result
    

 # Write code here 
[m,n] = input().split(' ')
inn=[]
for i in range(int(m)):
    inn.append(input().split(' '))

#print(inn)

output = main(inn)
for i in range(len(output)):
    for j in range(len(output[i])):
        if j != len(output[i])-1:
            print(output[i][j],end=' ')
        else:
            if i == len(output)-1 and j == len(output[i])-1:
                print(output[i][j],end='')
            else:
                print(output[i][j])

