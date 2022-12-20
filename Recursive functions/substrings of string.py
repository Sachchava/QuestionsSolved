def su(s,os,i):
    if i==len(s):
        print(os)
        if len(os)>0:
            print(ord(os))
        return 
    su(s,os,i+1)
    su(s,os+s[i],i+1)
def suu(s,a):
    if len(s)==0:
        print(a)
        # print(ord(a))
        return 
    c = s[0]
    code = int(s[0])
    suu(s[1:],a)
    suu(s[1:],a+s[0])
    suu(s[1:],a+str(code))
s = "abc"
os = ""
i = 0
# print(su(s,os,i))
print(suu(s,""))
# print(suu(s,""))