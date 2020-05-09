import datetime
year = 2016
def day(year):
    inn = datetime.date(year, 1, 1) 
    day = inn.strftime("%A")
    return day
def check_leap(year): 
    if (year % 4) == 0: 
        if (year % 100) == 0: 
            if (year % 400) == 0: 
                return True
            else: 
                return False
        else: 
             return True
    else: 
        return False

        
flag = True
k = year
while(flag == True):
    k = k + 1
    if day(year) == day(k):
        if check_leap(year) == check_leap(k):
            flag = False
        
print(k)




