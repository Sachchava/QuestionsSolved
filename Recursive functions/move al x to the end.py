def m(s):
    if len(s)==1:
        return s
    if s[0]=="x":
        return m(s[1:])+s[0]
    else:
        return s[0]+m(s[1:])
s = "axxxxxxxxbxx"
print(m(s))