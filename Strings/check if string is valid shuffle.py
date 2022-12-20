a = "Xy"
a = a.lower()
b = "12"
b = b.lower()
c = "Y21X"
c = c.lower()
if len(c)!=len(a+b):
    print("galat hai")
else:
    for i in range(len(c)):
        if c[i] in a or c[i] in b:
            print("valid shuffle")
        else:
            print("not a valifd shuffle")