from __future__ import print_function
number = 2
#print "{0:d}".format(number)
#print int(oct(number))
temp = str(hex(number))
temp = temp.split("x")
num = temp[1]
#print num
#print "{0:b}".format(number)

for i in range(1,number+1):
    decimalNum = "{0:d}".format(i)
    octNumber = int(oct(i))
    tempString = str(hex(i))
    tempString = tempString.split("x")
    hexNumber = tempString[1]
    binNumber = "{0:b}".format(i)
    print (decimalNum,end=' ')
    print (octNumber,end=' ')
    print (hexNumber,end=' ')
    print (binNumber,end='')
    print()

'''
width = len("{0:b}".format(n))
for i in xrange(1,n+1):
  print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=width)
'''
    
