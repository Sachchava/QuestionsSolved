def p(n,s):
    if n==0:
        return 
    p(int(n/10),s)
    
    print(s[int(n%10)])
n = 423
s = ["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
p(n,s)