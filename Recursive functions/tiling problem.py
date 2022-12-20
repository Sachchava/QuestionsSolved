def t(n):
    if n==1 or n==0:
        return n
    return t(n-1)+t(n-2)
print(t(4))