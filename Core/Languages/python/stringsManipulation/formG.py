from __future__ import print_function
input = row= 7
col = row -1
half = (row-1)/2
top_bottom = row-4
for i in range(row):
    for j in range(col):
        if (i == 0 or i == row-1) and (j >= 2 and j <col-1):
            print ('*',end='')
        elif i < row-1 and i>0:
            if j == 1:
                print ('*',end='')
            elif i == half and j >= col/2:
                print('*',end='')
            elif i > half and j == col-1:
                print('*',end='')
            else:
                print(' ',end='')
        else:
            print(' ',end='')
    print ('')
