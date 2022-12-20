import math
x = int(input("enter a no."))
n = int(math.sqrt(x))
if n*n==x:
    print(n-1)
else:
    print(n)