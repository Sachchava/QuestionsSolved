def binary(s):
    s = set(s).issubset({'0','1'})
    if s == True:
        print('binary')
    else:
        print('not binary babe')    
s = 'sa000'
binary(s)