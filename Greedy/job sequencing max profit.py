class solution:
    def maxprofit(self,arr):
        n = arr[0][1]
        a = []
        for i in range(n):
            a.append(0)
        # print(a)
        return a
    def profitfind(self,ar,arr):
        c= 0
        if ar !=[]:
            for i in range(len(arr)):
                n = arr[i][1]-1
                if ar[n]==0:
                    ar[n]=arr[i][2]
                    c+=1
                elif ar[n]!=0:
                    if ar[n-1]==0:
                        ar[n-1] = arr[i][2]
                        c+=1
                    if ar[n]<arr[i][2]:
                        ar[n]=arr[i][2]
                        
        return ar,c
    def profitfinder(self,ar,arr):
        s = 0
        for i in range(len(ar)):
            n = arr[i][1]-1
            if ar[n]==0:
                ar[n]=arr[i][2]
                s+=arr[i][2]
            elif ar[n]!=0:
                
                if ar[n-1]==0:
                    ar[n-1]=arr[i][2]
                    s+=arr[i][2]
                elif ar[n-1]!=0:
                    for j in range(n,-1,-1):
                        if ar[j]==0:
                            ar[j]=arr[i][2]
                            s+=arr[i][2]
                            break
                # if ar[n]<arr[i][2]:
                #     ar[n] = arr[i][2]
        return ar,s
if __name__ == "__main__":
    arr = [(1,7,100),(1,7,100),(1,7,100),(1,7,100),(2,1,19),(3,3,27),
        (4,2,25),(5,7,15)]
    arr = (sorted(arr,reverse = True,key = lambda c:c[1]))
    print(arr)
    ar = (solution().maxprofit(arr))
    print(ar)
    arr = sorted(arr,reverse = True,key = lambda x:x[2])
    print(arr)
    # print(solution().profitfind(ar,arr))
    print(solution().profitfinder(ar,arr))    