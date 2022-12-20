class solution:
    def maxstocks(self,arr,k):
        stocks = 0
        dup = arr
        arr = sorted(arr)
        print(arr)
        for i in range(len(arr)):
            P = min(dup.index(arr[i])+1, k//arr[i])
            print(P)
            stocks += P
            k -= (P * arr[i])
        return stocks
    def buyMaximumProducts(self,n, k, price):
 
    # Making pair of stock cost and day number
        arr = []
        
        for i in range(n):
            arr.append([i + 1, price[i]])
    
        # Sort based on the price of stock
        arr.sort(key = lambda x: x[1])
        
        # Calculating the max stocks purchased
        total_purchase = 0
        for i in range(n):
            P = min(arr[i][0], k//arr[i][1])
            total_purchase += P
            k -= (P * arr[i][1])

        return total_purchase
if __name__ == '__main__':
    arr = [10, 7, 19]
    k = 45
    print(solution().maxstocks(arr,k))
    print(solution().buyMaximumProducts(len(arr),k,arr))