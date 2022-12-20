class solution:
    def mindifference(self,arr,m):
        arr = sorted(arr)
        print(arr)
        minv = arr[len(arr)-1]-arr[0]
        if m == len(arr):
            return minv
        for i in range(len(arr)-m+1):
            # print(arr[i+(m-1)]-arr[i])
            if arr[i+(m-1)]-arr[i]<minv:
                print(arr[i+(m-1)],arr[i])
                minv = arr[i + m - 1] - arr[i]
        return minv
    def findMinDiff(self,arr, n, m):
        if (m==0 or n==0):
            return 0
        arr.sort()
        if (n < m):
            return -1
        min_diff = arr[n-1] - arr[0]
        for i in range(len(arr) - m + 1):
            min_diff = min(min_diff ,  arr[i + m - 1] - arr[i])
        return min_diff

if __name__ == "__main__":
    arr = [7, 3, 2, 4, 9, 12, 56]
    m = 3
    print(solution().mindifference(arr,m))
    print(solution().findMinDiff(arr,len(arr),m))