def special(s):
    m = ('[<>?||_()*&^%$#@!):{}]')
    s = set(s)
    if s.difference(m):
        print('string has special charectars')
    else:
        print('string does not have any special charecters')
s = 'satishboora45@'
special(s)



