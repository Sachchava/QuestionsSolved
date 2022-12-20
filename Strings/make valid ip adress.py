snew = "25525511135"
sz= len(snew)
l = []
for i in range(1, sz - 2):
    for j in range(i + 1, sz - 1):
        for k in range(j + 1, sz):
            snew = snew[:k] + "." + snew[k:]
            snew = snew[:j] + "." + snew[j:]
            snew = snew[:i] + "." + snew[i:]
            print(snew)