def c(n):
    if n==0:
        return 
    c(n-1)
    print(n)
n = 5
c(n)