class solution:
    def maxsumpairs(self,a,b):
        a = sorted(a)
        b = sorted(b)
        s = 0
        for i in range(len(a)):
            s+=abs(a[i]-b[i])
        return s
if __name__ == "__main__":
    ar1 = [4, 1, 8, 7]
    ar2 = [2, 3, 6, 5]
    print(solution().maxsumpairs(ar1,ar2))