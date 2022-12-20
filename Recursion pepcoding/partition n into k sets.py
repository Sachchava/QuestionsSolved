class solution:
    def partition(self,i,n,k,ans,ssf):
        if i>n:
            if ssf==k:
                print(ans)
            return
        for j in range(len(ans)):
            if len(ans[j])>0:
                ans[j].append(i)
                self.partition(i+1,n,k,ans,ssf)
                ans[j].pop()
            else:
                ans[j].append(i)
                self.partition(i+1,n,k,ans,ssf+1)
                ans[j].pop()
                break
if __name__ == "__main__":  
    n = 3
    k = 2
    ans = [[] for i in range(k)]
    solution().partition(1,n,k,ans,0)