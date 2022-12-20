class solution:
    def equalsum(self,arr,i,n,k,subsetsum,ans,ssf):
        if i==n:
            if ssf == k:
                f = True
                for i in range(len(subsetsum)-1):
                    if subsetsum[i]!=subsetsum[i+1]:
                        f = False
                        break
                if f :
                    print(ans)
            return 
        for j in range(len(ans)):
            if len(ans[j])>0:
                ans[j].append(arr[i])
                # print(subsetsum[j])
                q = subsetsum[j].pop()
                s = arr[i] + q 
                subsetsum[j].append(s)
                self.equalsum(arr,i+1,n,k,subsetsum,ans,ssf)
                ans[j].pop()
                w = subsetsum[j].pop()
                e =  w - arr[i]
                subsetsum[j].append(e)
                # subsetsum[j] -= arr[i]
            else:
                ans[j].append(arr[i])
                subsetsum[j].append(arr[i])
                self.equalsum(arr,i+1,n,k,subsetsum,ans,ssf+1)
                ans[j].pop()
                subsetsum[j].pop()
                break

if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    k = 3
    ans = [[] for i in range(k)]
    subsetsum = [[] for i in range(k)]
    summ = 0
    for i in arr:
        summ+=i
    if k == 1:
        for i in arr:
            print(i)
    elif k > len(arr) or summ%k !=0:
        print(-1)
    else:
        solution().equalsum(arr,0,len(arr),k,subsetsum,ans,0)