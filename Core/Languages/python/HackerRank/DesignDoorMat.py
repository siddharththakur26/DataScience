from __future__ import print_function
'''
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------
'''

string = "WELCOME"
design1 = ".|."
design2 = "-"
N = 7
M = 21
k = len(design1)
for i in range(1,N,2):
    print ((design1 *i).center(M,design2))
print (string.center(M,'-'))        
for i in range(N-2,-1,-2):
    print ((design1 *i).center(M,design2))