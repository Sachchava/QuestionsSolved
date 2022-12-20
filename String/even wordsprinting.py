def words(s):
    ns = s.split()
    print(ns)
    l = len(ns)
    print(l)
    for i in range(0,l):
        if len(ns[i])%2==0:
            print(ns[i])
s = 'satish is a ads good booi '
words(s)