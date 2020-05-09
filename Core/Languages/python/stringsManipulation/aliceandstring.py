'''in1= "abaca"
in2 = "cdbda"
flag = True
if in1 != in2 and len(in1)==len(in2):
    val1 = ord(in1[0])
    val2 = ord(in2[0])
    diff = val2-val1
    for i in range(1,len(in1)):
        val1 = ord(in1[i])
        val2 = ord(in2[i])
        if diff < (val2-val1):
            flag = False
            break
elif len(in1)!=len(in2):
    flag = False

if flag == True:
    print("YES")
else:
    print("NO")

'''
'''in1 ="sid"
print(in1[::-1])'''

"""in1="AMbuj verma"
temp = in1.lower()
val=""
out=""
for i in temp:
    if i == " ":
        out += "$"
    elif i.isalpha():
        val = str(ord(i)-96)
        out = out + val
        
print(out)
"""
"""out=[]
arr=["zazabcdefghgfgfededededcdefghghijkjihihgfe"]
for word in arr:
    flag = True
    word_length = len(word)
    for index in range(word_length-1):
        if (word[index] == 'z' and word[index+1] == 'a') or (word[index] == 'a' and word[index+1] == 'z'):
            diff = 1
        else:
            diff = abs(ord(word[index]) - ord(word[index+1]))
        
        if diff !=1:
            flag = False
            break
        
    if flag == False:
        out.append("NO")
    else:
        out.append("YES")
    
for i in out:
    print(i)"""


"""def size(string,number):
    form=""
    arr=[]
    for index in range(len(string)):
        if string[index] ==number:
            form += string[index]
            if index == len(string)-1:
                arr.append(form)
        elif string[index] !=' ':
            arr.append(form)
            form=""
    return arr



n = 5
string = "1 1 0 0 1 0 1 1 1 1"
form_1=""
form_0=""
arr=[]
arr_1 = size(string,'1')
#arr_1 = size(string,0)
print(arr_1)
#print(arr_1)

    
    



blocks_0 = size(string,'1')
blocks_1 = size(string,'0')

if blocks_0 >= blocks_1:
    print(blocks_0)
else:
    print(blocks_1)

"""






"""
arr_index_0=[]
arr_index_1=[]
for index in range(len(string)):
    if string[index] == '0':
        arr_index_0.append(index)
    elif string[index]=='1':
        arr_index_1.append(index)
count_0=0
count_1=0
for i in range(len(arr_index_0)-1):
    diff = abs(arr_index_0[i]-arr_index_0[i+1])
    if diff == 2:
        count_0 +=1
    else:
        count_0=0
for i in range(len(arr_index_1)-1):
    diff = abs(arr_index_1[i]-arr_index_1[i+1])
    if diff == 2:
        count_1 +=1
    else:
        count_1 = 0
if count_0 >= count_1:
    print(count_0+1)
else:
    print(count_1+1)"""

"""fav_string = "abcd"
arr=["ab","ef"]
out =0
for i in arr:
    flag = True
    for j in i:
        if fav_string.find(j) == -1:
            flag = False
            break
    if flag == True:
        out += 1

print(out)"""

"""number = "0123456789"

length = len(number)
prefix = number[0]
if length == 10 and number.isnumeric() and prefix !=0:
    print("YES")
else:
    print("NO")"""

"""last_num = 9
for i in range(1,last_num+1):
    flag=0
    for j in range(1,i+1):
        if i%j == 0:
            flag +=1
    if flag == 2:
        print(i)"""

"""inn = 100
sum = 0

while(inn>0):
    rem = inn%10
    inn = inn//10
    sum += rem
    if len(str(sum)) > 1:
        inn = sum
        sum=0

print(sum)"""

"""
arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,14,12]
length = len(arr)
index_arr=[]
for i in range(1,length+1):
    flag=0
    for j in range(1,i+1):
        if i%j == 0:
            flag +=1
    if flag == 2:
        index_arr.append(i)
#print(index_arr)
sum=0
for index in index_arr:
    sum += arr[index]
print(sum)
"""

