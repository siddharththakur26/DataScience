s = "aaabccddd"
#s = "a"
ans=[]
for  character in s:
    if not ans:
        ans.append(character)
    else:
        if ans[-1] == character:
            ans.pop()
        else:
            ans.append(character)
print "".join(ans)



