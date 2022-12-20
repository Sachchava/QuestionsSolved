a = [[1,3,5,7],
    [10,11,16,20],
    [23,30,34,60]]
x = 231
def aa(a,x):
    r = len(a)
    c = len(a[0])
    low = 0
    high = (r*c)-1
    while low<=high:
        mid = int((low+high)/2)
        if a[int(mid/c)][int(mid%c)]==x:
            return True
        elif a[int(mid/c)][int(mid%c)]>x:
            high = mid-1
        else:
            low = mid+1
    return False
print(aa(a,x))
# def aa(a,x):
#     r = len(a)
#     c = len(a[0])
#     for i in range(r):
#         for j in range(c):
#             if a[i][j]==x:
#                 return True
#     return False
# print(aa(a,x))
