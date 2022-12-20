f = [1,2,3]
j = [1,2,3]
k = [1,2,3]
b = []
def e(f,j,k,b):
    for m in f:
        for n in j:
            for o in k:
                if m!=n and n!=o and o!=m:   
                    b.append([m,n,o])
    for i in range(0,len(b)):
        if b[i] == f:
            bb = b[i+1]
    return bb
                
print(e(f,j,k,b))