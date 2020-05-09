'''
This is a simple string decoding algorithm. The idea is to take a string of characters and decode it into an array. Each character is a single element in the result unless a backslash followed by a positive number is encountered.

When a backslash followed by a positive number is found, the number indicates how many of the next characters are grouped together as one element.

"abc\5defghi\2jkl" => [ "a", "b", "c", "defgh", "i", "jk", "l" ]
"\5ab\3cde" => [ "ab\3c", "d", "e" ]


'''

import re
def decode(string):
    # write your code
    X = list(string)
    #print(X)
    val ='0'
    res=""
    o=[]
    flag = 0
    for index, i in enumerate(X):          
            if i == "\\" and val=="0":
                ti = index
                while(X[ti+1].isdigit()):
                    val += X[ti+1]
                    ti +=1
                flag =index+len(val)
            
            elif flag <= index  and int(val)>0:
                res += i
                val = str(int(val)-1)
                if int(val) == 0 or index == len(X)-1:
                    o.append(res)
                    res=""
                  
            elif int(val)==0:
                    o.append(i)

    return o

print(decode(""))
#print(decode("\\10a\\1bc"))
#print(decode("abc\\5defghi\\2jkl"))            

