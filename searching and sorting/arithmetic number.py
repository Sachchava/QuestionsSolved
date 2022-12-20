a = 1
b = 2
c = 3
def y(a,b,c):
    if c==0:
        if b == a:
            return 1
        else:
            return 0
    else:
        if (b-a)/c<0:
            return 0
        else:
            if (b-a)%c==0:
                return 1
            else:
                return 0
print(y(a,b,c))