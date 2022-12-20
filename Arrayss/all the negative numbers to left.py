a = [-7,56,9,-6,0,3,-7]
b = []
for i in range(0,len(a)):
    m = min(a)
    b.append(m)
    a.remove(m)
print(b)
# p = 0 
# for i in range(0,len(a)):
#     for j in range(i,len(a)):
#         if a[i]<a[j]:
#             continue
#         else:
#             a[i],a[j]=a[j],a[i]
