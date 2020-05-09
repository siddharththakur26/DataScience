s = "heelo  12orld lol"
tempNames = s.split(" ")
names =[]
print(tempNames)
for i in tempNames:
    name = i
    if name != '':
        if i[0].isalpha():
            tempName = i
            tempLetter = i[0].upper()
            name = tempLetter+i[1:]
    names.append(name)
print (" ".join(names))       
