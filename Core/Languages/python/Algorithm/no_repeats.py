'''
                                Algorithms: No Repeats Please

Return the number of total permutations of the provided string 
that don't have repeated consecutive letters.
Assume that all characters in the provided string are each unique.

For example, aab should return 2 because it has 6 total permutations 
(aab, aab, aba, aba, baa, baa), but only 2 of them (aba and aba) don't have 
the same letter (in this case a) repeating.
'''

string = "aab"
flag_repeat=0
temp_set=set()
occurances=[]
for i in string:
    if string.count(i)>1 and i not in temp_set:
        occurances.append(string.count(i))
        temp_set.add(i)
        flag_repeat +=1
    

print(occurances)

def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

def denominator_fact(occurances):
    denominator=1
    for i in range(len(occurances)):
        denominator = denominator * fact(occurances[i])
    return denominator

total_permutation = fact(len(string))
#print(total_permutation)


eval =[]
for i in range(flag_repeat):
    if i < flag_repeat-1:
        num = fact(len(string)-(i+1))
        occurances.pop(0)
        den = denominator_fact(occurances)
        repeated_permutation = num/den
        total_permutation_without_repeatation = flag_repeat*repeated_permutation
        eval.append(total_permutation_without_repeatation)
    else:
        eval.append(fact(len(string)-(i+1)))

for index,val in enumerate(eval):
    if index == 0 or index == len(eval)-1:
        total_permutation = total_permutation - val
    else:
        total_permutation = total_permutation + val

print(total_permutation)
    




    