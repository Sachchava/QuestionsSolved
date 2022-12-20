def aa(a,oa,i):
    if i==len(a):
        print(oa)
        return 
    aa(a,oa,i+1)
 
    aa(a,oa+a[i],i+1)
a = "abc"
oa = ""
i = 0
aa(a,oa,i)