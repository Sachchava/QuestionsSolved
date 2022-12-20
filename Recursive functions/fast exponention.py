def ee(n,e):
    if e == 0:
        return 1
    next = ee(n,e-1)
    return n*next
n = 2
e = 5
print(ee(n,e))
# def eee(n,e):
#     if n==0:
#         return 1
#     next = int(eee(n,e/2))
#     if n%2==0:
#         return n*next*next
#     else:
#         return next*next
