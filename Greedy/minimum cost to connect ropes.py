import heapq
class solution:
    def mincost(self,arr):
        arr.sort()
        print(arr)
        s = arr[0]+arr[1]
        res = [s]
        for i in range(2,len(arr)):
            s+=arr[i]
            res.append(s)
        # print(s)
        print(sum(res),res)
    def minvalue(self,arr):
        res = []
        while len(arr)!=1:
            value1 = min(arr)
            arr.remove(value1)
            value2 = min(arr)
            arr.remove(value2)
            add = value1+value2
            arr.append(add)
            res.append(add)
        print(sum(res))
    def minCost(self,arr,n) :
        res = 0
        heapq.heapify(arr)
        while len(arr)!=1:
            value1 = heapq.heappop(arr)
            value2 = heapq.heappop(arr)
            data = value1+value2
            res+=data
            heapq.heappush(arr,data)
        return (res)
if __name__ == "__main__":
    arr = [4, 2, 3, 6]
    # solution().mincost(arr)
    # solution().minvalue(arr)
    print(solution().minCost(arr,len(arr)))