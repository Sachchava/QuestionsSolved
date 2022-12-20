a = 5
def aa(a):
    if a==0:
        return 1
    return a * aa(a-1)
print(aa(a))