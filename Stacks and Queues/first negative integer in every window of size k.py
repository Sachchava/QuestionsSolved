from collections import deque
class solution:
    def firstnegative(self,arr,k):
        q = []
        for i in range(len(arr)):
            if arr[i]<0:
                q.append(i)
        if len(q)==0:
            return [0 for i in range((len(arr)%k)+1)]
        i = 0
        j = k
        p = 0
        res = []
        while j<len(arr)+1:
            if q[p]<i:
                q.pop(0)
            if len(q)==0:
                res.append(0)
                i+=1
                j+=1
                
            elif q[p]>=i and q[p]<j:
                res.append(arr[q[p]])
                i+=1
                j+=1
            else:
                res.append(0)
                i+=1
                j+=1
        return res

if __name__ == "__main__":
    arr = [-458,-598,-79,544,4,954,954,4]
    k = 3
    print(solution().firstnegative(arr,k))