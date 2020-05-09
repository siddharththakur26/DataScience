def main():
    inn = input()
    alpha_flag =numeric_flag=dot_flag=negative_flag=0
    ty=""
    for i in inn:
        if i.isalpha():
            alpha_flag +=1
        elif i.isnumeric():
            numeric_flag +=1
        elif i == '.':
            dot_flag +=1
        elif i == '-':
            negative_flag +=1
    if alpha_flag == len(inn):
        ty="string"
    elif numeric_flag == len(inn) or (numeric_flag + negative_flag)== len(inn):
        ty="Integer"
    elif (numeric_flag+dot_flag)==len(inn) or (numeric_flag+dot_flag+negative_flag)==len(inn):
        ty= "Float"
    
    if ty=="":
        return "This is something else."
    else:
        return "This input is of type "+ty+"."

 # Write code here 

print(main())