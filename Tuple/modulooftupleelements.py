from operator import mod
def modd(t,tt):
    return tuple(map(mod,t,tt))
t = (10,20,30,44,50)
tt = (5,5,5,5,5)

print(modd(t,tt))