b = 9
keyboards = [4]
drives =  [5]
storeExpenses= []
for i in keyboards:
    for j in drives:
        if (i+j) < b:
            storeExpenses.append(i+j)
        else:
            storeExpenses.append(-1)
print sorted(storeExpenses)[len(storeExpenses)-1]
