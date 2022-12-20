a = ["for","geek" , "geek", "for", "geek", "aaa"]
cc = {0}
b = []
for i in range(len(a)):
    c = 0
    for j in range(i,len(a)):
       if a[i]==a[j]:
           c+=1
           if a[i] not in b:
               b.append(a[i])
    cc.add(c)    
print(b,cc)