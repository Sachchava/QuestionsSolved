def greaterwords(s):
    s = s.split()
    print(s)
    l = len(s)
    
    for i in range(0,l):
        if len(s[i])>=k:
            print(s[i])
            i+=1


s = 'satish is a good boy'
k = 4
greaterwords(s)