from heapq import heappush,heappop
class solution:
    def ksorted(self,arr):
        n = len(arr)
        q = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                heappush(q,arr[i][j])
        for i in range(n*n):
            print(heappop(q))
    def ksorted1(self,arr):
        pq = []
        size = 0
        for i in range(len(arr)):
            heappush(pq,[arr[i][0],i])
            size+=len(arr[i])
        print(pq)
        ind = 0
        while size!=0:
            ele = heappop(pq)
            # print(arr[ele[1]][ind:])
            ind = arr[ele[1]][ind:].index(ele[0])
            # ind+=1
            p = arr[ele[1]][ind]
            heappush(pq,[p,ele[1]])
            print(ele)
            size-=1
            arr[ele[1]] = arr[ele[1]][ind+1:]

if __name__ == "__main__":
    arr = [[1,2,3,4],[2,2,3,4],[5,5,6,6],[7,8,9,9]]
    solution().ksorted1(arr)