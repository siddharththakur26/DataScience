# Actual Return
d1 = 2
m1 = 7
y1 = 1014
#Expected Return
d2 = 1
m2 = 1
y2 = 1014
fine = 0
if y1 > y2:
    fine = 10000
elif y1 == y2 and m1>m2:
    diff = m1 - m2
    fine = 500 * diff
elif y1 == y2 and m2 == m1 and d1>d2:
    diff = d1 - d2
    fine = 15 * diff
print fine
