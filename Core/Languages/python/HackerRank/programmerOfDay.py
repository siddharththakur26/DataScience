dict = {
    '01':31,
    '02':28,
    '03':30,
    '04':31,
    '05':30,
    '06':31,
    '07':31,
    '08':31,
    '09':30,
    '10':31,
    '11':30,
    '12':31
}

year = 1918


#print dict['02']

day = 256
if year >=1700 and year <= 1917:
    if year%4==0:
        dict['02'] = 29
elif year >=1919:
    if year%400==0 or(year%4 == 0 and year%100 != 0):
        dict['02'] = 29

sumDays = 0
month=1

for key,value in sorted(dict.items()):
    sumDays += value
    
    if sumDays >= 256:
        sumDays -= value
        month = key
        break
    


print sumDays
day = day - sumDays
if year == 1918:
    day = day + 13
#print month
print str(day) + '.' +  str(month) +'.'+str(year)

    
