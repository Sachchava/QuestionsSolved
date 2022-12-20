a = "0001010111"
c2 = 0
c1 = 0
for i in range(len(a)):
  
    if i%2==0 :
        if a[i]!="0":
            c1+= 1
        else:
            c2+=1
    if i%2!=0 :
        if a[i]!="1":
            c1+=1
        else:
            c2+=1
print(min(c1,c2))
print(c2)