from heapq import heappush,heappop
class solution:
    def smallestele(self,k,n,arr):
        q = []
        for i in range(k):
            for j in range(n):
                heappush(q,(arr[i][j],i))
        print(q)   
        # print(sorted(q))
        for i in range(len(q)):
            print(heappop(q),end = " ")
if __name__ == "__main__":
    k = 3 
    n = 5
    arr =  [[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]]
    solution().smallestele(k,n,arr)