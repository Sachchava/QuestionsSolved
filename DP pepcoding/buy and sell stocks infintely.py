class solution:
    def maxprofit(self,arr):
        maxxp = 0
        for i in range(len(arr)-1):
            if arr[i+1]>=arr[i]:
                maxxp += arr[i+1]-arr[i] 
          
                
        return maxxp
if __name__ == "__main__":
    arr = [11,6,7,19,4,1,6,18,4]
    print(solution().maxprofit(arr))