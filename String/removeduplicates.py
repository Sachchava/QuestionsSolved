def duplicates(s):
    s = set(s)
    s = ''.join(s)
    print('unsorted order\n'+ str(s))
    s = sorted(s)
    s = ''.join(s)
    #print('sorted order \n'+ str(s))
    print(''.join(s))

s = 'satish'
duplicates(s)    