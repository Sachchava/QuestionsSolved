def re(s):
    if len(s)==1:
        return s
    if s[0]==s[1]:
        return re(s[1:])
    else:
        return s[0]+re(s[1:])
s = "aacb"
print(re(s))