t = [(1, 42, 2), (54, 6, 67), (5, 47, 5)]
ad = 5
for m in t:
    for n in m:
        n = n + ad
        print(tuple(n))
