class solution:
    def maxsum(self,ar):
        ar = sorted(ar)
        s = 0
        for i in range(len(ar)):
            s+=ar[i]*i
        return s%(10**9+7)
if __name__ == "__main__":
    ar = [5, 3, 2, 4, 1]
    print(solution().maxsum(ar))