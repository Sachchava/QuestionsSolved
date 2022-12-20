class solution:
    def mincost(self,x,y,m,n):
        hor = 1
        ver = 1
        i = 0
        j = 0
        ans = 0
        x = sorted(x,reverse = True)
        y = sorted(y,reverse = True)
        while i<m and j<n:
            if x[i]>y[j]:
                ans += x[i]*ver
                hor+=1
                i+=1
            else:
                ans+=y[j]*hor
                ver+=1
                j+=1
        while i<m:
            ans+=x[i]*ver
            hor+=1
            i+=1
        while j<n:
            ans+=y[j]*hor
            ver+=1
            j+=1
        return ans
if __name__ == "__main__":
    x = [2, 1, 3, 1, 4]
    y = [4, 1, 2]
    print(solution().mincost(x,y,len(x),len(y)))