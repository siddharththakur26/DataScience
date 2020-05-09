
def main():
    n = input()
    cnt_alpha=cnt_upper=0
    for i in n:
        if i.isalpha():
            cnt_alpha +=1
            if i.isupper():
                cnt_upper +=1
    
    print(cnt_upper)
    print(cnt_alpha-cnt_upper)

 # Write code here 

main()