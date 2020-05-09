import datetime
def main(m,d):
    days_arry = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    inn = datetime.date(2017, m, d) 
    day = inn.strftime("%A")
    for i in range(len(days_arry)):
        if days_arry[i] == day:
            index = i
            break

    return  index+1

m = int(input())
d = int(input())

print(main(m,d),end='')