a = 81
b = 81
def factors(temp):
    number=[]
    i=2
    while(temp >1): 
        if temp % i==0:
            temp = temp / i
            number.append(i)
            i = 2
        else:
            i +=1
    return number

def set_factors(factors):
    return set(factors)

factors1 = factors(a)
factors2 = factors(b)

set_factors1 = set_factors1(factors1)
set_factors2 = set_factors2(factors2)

def count_factors(set_factors):
    count_fact = []
    for i in set_factors:
        count_fact.append(set_factors.count(i))
    return count_fact

count_factors1=count_factors(set_factors1)
count_factors2=count_factors(set_factors2)

if len(count_factors1)>len(count_factors2):
    for i in range(len(count_factors2)):
        if count_factors1[i] > count_factors2[i]:
            


    


    