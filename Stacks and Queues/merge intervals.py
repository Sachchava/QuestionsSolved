class solution:
    def merge(self,arr):
        arr = sorted(arr,key = lambda x:x[0])
        print(arr)
        res = set()
        i = 0
        j = 1
        for i in range(len(arr)):
            if arr[i][1]>arr[j][0]:
                arr[i][1]=max(arr[j][1],arr[i][1])
                res.add(arr[i][1])
        # return res

if __name__ == "__main__":
    arr =  [[6, 8], [1, 9], [2, 4], [4, 7]]
    # arr = [[1,3],[2,4],[6,8],[9,10]]
    print(solution().merge(arr))