def uncommon(s,m):
    s = s.split()
    m = m.split()
    l = len(m)
    ll = len(s)
    i = 0
    for i in range(l):
        if m[i] in s:
            i+=1
        else:
            print(m[i])
    for j in range(ll):
        if s[j] in m:
            j+=1
        else:
            print(s[j])

m = 'apple banana mango'
s = 'banana sheru peru apple bobo '
uncommon(s,m)