def f(n):
    if n==0 or n==1 or n==2:
        return n
    return f(n-1)+f(n-2)*f(n-1)
print(f(3))