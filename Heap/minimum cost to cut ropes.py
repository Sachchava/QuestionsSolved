from heapq import heappush,heappop
class solution:
    def minimumcost(self,arr):
        res = 0
        ans = 0
        pq = []
        for i in range(len(arr)):
            heappush(pq,arr[i])
 
        while pq!=[]:
            try:
                el1 = heappop(pq)
            except:
                el1 = 0
            try:
                el2 = heappop(pq)
            except:
                el2 = 0
            
            sum = el1+el2
            ans +=sum
            if pq == []:
                break
            heappush(pq,sum)
        # while(len(arr) > 1):
         
        # # Extract shortest two ropes from arr
        #     first = heappop(arr)
        #     second = heappop(arr)
            
        #     #Connect the ropes: update result
        #     # and insert the new rope to arr
        #     res += first + second
        #     heappush(arr, first + second)
         
        # return res
        print(ans)
if __name__ =="__main__":
    arr = [4]
    (solution().minimumcost(arr))