class solution:
    def nextsmaller(self,arr):
        res = []
        stack = []
        pos = -1 
        pos-=1
        for i in range(len(arr)-1,-1,-1):
            if stack == []:
                res.insert(pos,-1)
                pos-=1
                stack.append(arr[i])
            else:
                while True:
                    if stack[-1]>arr[i]:
                        stack.pop()
                    if stack == []:
                        res.insert(pos,-1)
                        pos-=1
                        stack.append(arr[i])
                        break
                    if stack[-1]<arr[i]:
                        res.insert(pos,stack[-1])
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
                        res.append(stack[-1])
                        stack.append(arr[i])
                        break
        return res

if __name__ == "__main__":
    arr = [ 1, 3, 0, 2, 5]
    print(solution().nextsmaller(arr))
    # print(solution().prevsmaller(arr))