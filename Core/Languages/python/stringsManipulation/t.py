"""def get_total_primes(a,b):
    X = [True for _ in range(b+1)]
    p=2
    while(p*p <= b):
        if X[p] == True:
            for i in range(p*p,b+1,p):
                X[i]=False
        p +=1
    arr= [2,3,5,7]
    cnt =0
    index = a +1
    for i in X[a+1:b+1]:
        if i == True:
            flag = True
            s = str(X[index])
            for j in s:
                if int(j) not in arr:
                    flag = False
            if flag==True:
                cnt +=1
        index +=1
    #print(X)
    return cnt
print(get_total_primes(10,100))

#print(get_total_primes(35880,9889973))


def SieveOfEratosthenes(n): 
      
    # Create a boolean array "prime[0..n]" and initialize 
    #  all entries it as true. A value in prime[i] will 
    # finally be false if i is Not a prime, else true. 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
          
        # If prime[p] is not changed, then it is a prime 
        if (prime[p] == True): 
              
            # Update all multiples of p 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
      
    # Print all prime numbers 
    for p in range(2, n): 
        if prime[p]: 
            print (p)


print(ord('z'))
def v(st):
    arr = ['a','e','i','o','u']
    mve = ['c', 'o', 'd','e']
    exc = {'c':1,'o':1,'d':3,'e':4}
    res=""
    for i in st:
        # consonent
        if i not in exc:
            if i not in arr:
                val = (ord(i)+9)         
                if val >= 123:
                    val = chr((val%123)+97)
                    #print(chr(val+97))
                else:
                    val = chr(val)
            elif i in arr:
                val = (ord(i)-5)
                if val < 97:
                    val = 97%val
                    val = chr(123-val)
                else:
                    val = chr(val)
            if val in mve:
                res +=i
            else:
                res += val
        else:
            val = ord(i) - exc[i]
            res += chr(val)
        
        
        
         
    return res

def sum_consecutives(s):
    #good luck
    res=[]
    prev=None
    val =0
    for index in range(len(s)-1):
        pres = s[index] 
        if index > 0:
            prev = s[index-1]

        if pres == prev:
            val += pres
        else:
            res.append(pres)
            val=0
      


    return res



print(sum_consecutives([1,4,4,4,0,4,3,3,1]))

def even_odd(arr):
    #your code here
    tot=0
    for index ,_ in enumerate(arr):
        if index > 0:
            if index%2!=0:
                tot *= arr[index]
            else:
                tot += arr[index]
        else:
            tot = arr[index]
    return tot
print(even_odd([1,2,6,1,6,3,1,9,6]))

import numpy
def rotate_in_place(matrix):
    matrix[:] = numpy.array(numpy.rot90(matrix,3)).tolist()
    return matrix

matrix = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

print(rotate_in_place(matrix))
print(matrix)
"""

map = [[True, False],[True, True]]
miner = {'x':0,'y':0}
exit = {'x':1,'y':1}
row = len(map)
col = len(map)
x = miner['x']
y = miner['y']
for i in range(row):
    for j in range(col[i]):    
        if x+1 > 0 and y +1 > 0 and x+1 < row and y+1 < col and x-1 > 0 and y -1 > 0 and x-1 < row and y-1 < col:
            while(True):
                Xn,Yn = map[x+1],map[y+1]


        
            



