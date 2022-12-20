def tr(s):
    a = {
    'm':1000,
    'c':100,
    'd':500,
    'x':10,
    'v':5,
    'i':1
    }
    s = s.replace("iv","iiii").replace("ix","viiii").replace("xl","xxxx").replace("xc","lxxxx").replace("cd","cccc").replace("cm","dcccc")
    n = 0
    for ele in s:
        n+= a[ele]
    return n
s = "MCMIV"
s = s.lower()
print(tr(s))