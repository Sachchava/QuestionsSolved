def re(s):
    if len(s)==0:
        return 
    if s[0]=="p"and s[1]=="i":
        print("3.14")
        re(s[2:])
    else:
        print(s[0])
        re(s[1:])
s = "pipeqpwqeqpi"
re(s) 