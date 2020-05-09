import textwrap
string = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
max_width = 4
# store in list
wrappedStrings = textwrap.wrap(string,max_width)
# store as strings
values =  textwrap.fill(string,max_width)