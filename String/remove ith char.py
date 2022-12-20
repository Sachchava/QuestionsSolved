def remove_i(s,i):
    l = len(s)
    s = s[:i] + s[i+1:l]
    print(s)



s = 'satishchandra'
i = 12
remove_i(s,i)