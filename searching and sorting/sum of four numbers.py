a = [0,0,2,1,1]
x = 3

s = []
a = sorted(a)
for i in range(len(a)):
    for j in range(i+1,len(a)):
        n = x-a[i]-a[j]
        low = j+1
        high = len(a)-1
        while low< high:
            b= []
            sum = a[low] +a[high]
            if sum<n:
                low+=1
            elif sum > n:
                high-=1
            elif sum ==n:
                b.append(a[i])
                b.append(a[j])
                b.append(a[low])
                b.append(a[high])
                s.append(b)
               
               
           
                break
print(s)