def vo(s):
    s = s.replace(' ','')
    s = s.lower() 
    vowel = (s.count('a'),s.count('e'),s.count('i'),s.count('o'),s.count('u'))
    print(vowel)
    if vowel.count(0)>0:
        return ('notaccepted')
    else:
        return ('accepted') 
s = 'u'
print(vo(s))        