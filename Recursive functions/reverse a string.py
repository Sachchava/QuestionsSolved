def re(s):
    if len(s)==0:
        return 
    r = s[1:]
    re(r)
    print(s[0])
s = "sati"
re(s)