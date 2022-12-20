def replacedc(s):
    
    s = s.replace(',','s')
    print(s)
    s = s.replace('.',',')
    print(s)
    s = s.replace('s','.') 
    print(s)
s = '12, 34. 546. 234, 234. '    
replacedc(s)