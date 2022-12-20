class solution:

    def platformsrequired(self,arr,dep):
        result = 1
        for i in range(len(arr)):
            plat = 1
            for j in range(i+1,len(arr)):
                if arr[i]>=arr[j] and arr[i]<=dep[j] or arr[j]>=arr[i] and arr[j]<=dep[i]:
                    plat+=1
            result = max(result,plat)
        return result
    def platformsfinder1(self,arr,dep):
        plat = 1
        result = 1
        i = 1
        j = 0
        while i<len(arr) and j<len(arr):
            if arr[i]<=dep[j]:
                plat+=1
                i+=1
            elif arr[i]>dep[j]:
                plat-=1
                j+=1
            if plat>result:
                result = plat
        return result
if __name__ == '__main__':
    arr = [900, 1100, 1235 ]
    dep = [1000, 1500, 1240]
    # a = solution().pairs(arr,dep)
    # a = sorted(a,key = lambda x:x[1])
    # print(a)
    b = solution().platformsrequired(arr,dep)
    bb = solution().platformsfinder1(arr,dep)
    print(b,bb,end = '\n')