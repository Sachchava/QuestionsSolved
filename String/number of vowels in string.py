def vowelnumber(s):
    s = set(s)
    print(s)
    ss = {'a','e','i','o','u'}
    i = 0
    l = len(s)
    print(l)
    for i in range(l):
        if s[i] in ss:
            i+=1

    print(i)        


s = 'satishCHANDRAAAAAA'
vowelnumber(s)