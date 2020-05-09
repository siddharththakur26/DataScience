'''
find how many times substrings has been come up in the string
'''
string= "ABCDCCDC"
sub_string = "CDC"
n = len(sub_string)
cnt = 0
for i in range(0,len(string)):
    tempString = string[i:i+n]
    if tempString == sub_string:
        cnt +=1
print cnt
