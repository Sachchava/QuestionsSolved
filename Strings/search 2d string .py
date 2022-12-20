a = ["DDDGDD","BBDEBS","BSKEBK",
            "DDDDDE","DDDDDE","DDDDDG"]
b = "GEEKS"
c = 0
for i in a:
    for j in i:
       for wl in range(len(b)):
           print(b[wl])
#            if b[wl] == j:
#                ii = a[i].index(b[wl])
#                a.pop(ii)
#                a.insert(ii,0)
#                c+=1
# print(c)
