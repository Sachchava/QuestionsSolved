s = "{{}{{{}{{}}{{"
a = ["{"]
c = 0
o = 0
for i in range(len(s)):
    if s[i] in a:
        o+=1
    else:
        c+=1
print((max(c,o))-(min(c,o))+1)