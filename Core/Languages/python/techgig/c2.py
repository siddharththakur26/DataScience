
def main():
    a = 1
    b = 20
    cnt=cnt_prime=0
    for i in range(a,b+1):
        for j in range(1,i+1):
            if i%j == 0:
                cnt +=1
        if cnt == 2:
            cnt_prime +=1
        cnt=0
    return cnt_prime
    



 # Write code here 

print(main(),end='')
print()