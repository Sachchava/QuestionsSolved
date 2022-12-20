def aa(n):
    if n<0:
        return 0
    if n==0:
        return 1
    return aa(n-1)+aa(n-2)+aa(n-3)
print((aa(4)))