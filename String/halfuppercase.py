def halfuppercase():
    l = len(s)
    m = int(l/2)
    w = s[:m] + s[m:l].upper()
    print(w)
   
s = 'satishchandra' 
halfuppercase()       