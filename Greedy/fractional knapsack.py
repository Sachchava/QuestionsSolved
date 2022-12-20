class solution:
    def pairs(seld,val,wt):
        res = []
        for i in range(len(wt)):
            res.append((val[i],wt[i]))
        return res
    def maxvalue(self,arr,wl):
        res = []
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if arr[i][1]+arr[j][1]<=wl:
                    res.append(arr[i][0]+arr[j][0])
                if arr[i][1]<=wl:
                    res.append(arr[i][0])
        return res
    def maxloot(self,wl,arr):
        w = 0
        s= 0
        for i in range(len(arr)):
            if w+arr[i][1]<=wl:
                w+=arr[i][1]
                s+=arr[i][0]
            elif w+arr[i][1]>wl:
                value = wl-w
                l = int(arr[i][0]/arr[i][1])
                s+=l*value
        return s




if __name__ == "__main__":
    values = [60,100,120]
    weight = [10,20,30]
    arr = solution().pairs(values,weight)
    arr = sorted(arr,key = lambda x:x[1])
    print(arr)
    wl = 50
    # print(solution().maxvalue(arr,wl))
    print(solution().maxloot(wl,arr))
