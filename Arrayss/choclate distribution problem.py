a = [3,4,1,9,56,7,9,12]
m = 5
p = 99999999999
q = []
a = sorted(a)
print(a)
for i in range(0,len(a)):
    for j in range(i+m-1,len(a)):
          k = a[j]-a[i] 
          q.append(k)
print(min(q))
          
              