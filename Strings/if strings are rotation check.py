a = "abcd"
b = "cdab"
if len(a)!=len(b):
    print(False)
else:
    
    aa = []
    for e in a:
        aa.append(e)
    print(aa)
    bb = []
    for e in b:
        bb.append(e)
    print(bb)
    for i in range(len(bb)):
        ch = bb[0]
        bb.pop(0)
        bb.append(ch)
        print(bb)
        if bb == aa:
            print("hogya")
        else:
            print("nhi hua")