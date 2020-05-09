input = [48,180]
divisor = 2

def factor(value,divisor):
    if value == 1:
        return arr
    quotient = value / divisor
    reminder = value % divisor    
    if reminder == 0:
        value = quotient
        arr.append(divisor)
    else:
        divisor = divisor + 1
    return factor(value,divisor)

def lcm(arr):
    uniqueFactors = set([])
    for i in arr:
        uniqueFactors.add(i)
    
    for i in uniqueFactors:
        count = arr.count(i)
        
factors= []
for i in input:
    arr = []
    factors.append(factor(i,divisor))
    lcm(arr)

    print arr



'''
import itertools
def lcm(factors):
    mergeFactors = list(itertools.chain.from_iterable(factors))
    uniqueFactors = set([])

    for i in mergeFactors:
        uniqueFactors.add(i)

    answer = 1

    for i in uniqueFactors:
        count = mergeFactors.count(i)
        temp = count / 2
        count = temp + (count%2)
        answer = answer * (i**count) 
    return answer

factors=[]
for i in input:
    arr = []
    factors.append(factor(i,divisor))
    print arr

lcmOfA = lcm(factors)
print lcmOfA
'''
############### Find GCD #####################


        
