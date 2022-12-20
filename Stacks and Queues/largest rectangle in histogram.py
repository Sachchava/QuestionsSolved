class solution:
    def nextsmaller(self,arr):
        res = []
        stack = []
        pos = -1
        for i in range(len(arr)-1,-1,-1):
            if stack == []:
                res.insert(pos,len(arr))
                pos-=1
                stack.append(arr[i])
            else:
                while True:
                    if arr[i]<=stack[-1]:
                        stack.pop()
                    if stack == []:
                        res.insert(pos,len(arr))
                        pos-=1
                        stack.append(arr[i])
                        break
                    if arr[i]>stack[-1]:
                        res.insert(pos,arr.index(stack[-1]))
                        pos-=1
                        stack.append(arr[i])
                        break
        return res
    def prevsmaller(self,arr):
        res = []
        stack = []
        for i in range(len(arr)):
            if stack == []:
                res.append(-1)
                stack.append(arr[i])
            else:
                while True:
                    if arr[i]<=stack[-1]:
                        stack.pop()
                    if stack==[]:
                        res.append(-1)
                        stack.append(arr[i])
                        break
                    if arr[i]>stack[-1]:
                        res.append(arr.index(stack[-1]))
                        stack.append(arr[i])
                        break
        return res
    def maxarea(self,arr,arr1,arr2):
        res = []
        for i in range(len(arr)):
            area = (arr1[i]-arr2[i]-1)*arr[i]
            res.append(area)
        return max(res)
# if __name__ == "__main__":
if __name__ == "__main__":
    arr = [436,832,55,324,356,967,131,999,192,212,649,646,127,710,65,125,234,39,287,256,557,954,475,471,5,847,168,571,380,983,520,536,420,529,121,464,695,137,484,519,404,585,829,841,859,724,862,14,429,190,341,45,901,75,347,959,705,967,727,156,901,943,439,907,857,422,998,585,999,806,290,811,33,512,32,393,952,944,748,396,369,450,720,20,962,452,920,196,665,399,850,642,351,268,983,367,897,760,127,113]
    arr1 = solution().nextsmaller(arr)
    arr2 = solution().prevsmaller(arr)
    print(solution().maxarea(arr,arr1,arr2))