def p(s,ind):
    if ind ==len(s):
        print(''.join(s))
        return
    for i in range(ind,len(s)):
        s[ind],s[i]=s[i], s[ind]
        p(s,ind+1)
        s[ind],s[i]=s[i], s[ind]
s = "abc"
s = list(s)
print(p(s,0))