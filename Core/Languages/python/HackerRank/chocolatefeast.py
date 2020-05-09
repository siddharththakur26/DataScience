n = 12 # budget
c = 4 # price per chocolate
m = 4 # price per chocolate

bars_eaten = n/c
wrappers = bars_eaten

while(wrappers >= m):
    quo = wrappers/ m
    reminder = (wrappers % m)
    bars_eaten = bars_eaten + quo
    wrappers = quo + reminder

print(bars_eaten)

    
    
