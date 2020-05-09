'''
Program to tell whether there exist a string character which is a alphanumeric, alphabet, digit,islowercase
, or uppercase. print True for these criteria
'''
s= "qA2"
flag = set()
for i in s:
    if i.isalnum():
        flag.add('1')
    if i.isalpha():
        flag.add('2')
    if i.isdigit():
        flag.add('3')
    if i.islower():
        flag.add('4')
    if i.isupper():
        flag.add('5')
#print flag
for i in range(1,6):
    if str(i) in flag:
        print True
    else:
        print False