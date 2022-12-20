class solution:
    def nextgreater(self,arr):
        stack = []
        res = []
        pos = -1
        for i in range(len(arr)-1,-1,-1):
            if stack==[]:
                res.insert(pos,-1)
                pos -=1
                stack.append(arr[i])
            else:
                while True:
                    if arr[i]>=stack[-1]:
                        stack.pop()
                    if stack==[]:
                        res.insert(pos,-1)
                        pos -=1
                        stack.append(arr[i])
                        break
                    if arr[i]<stack[-1]:
                        res.insert(pos,stack[-1])
                        pos -=1
                        stack.append(arr[i])
                        break
        return res    
    def prevgreater(self,arr):
        res = []
        stack = []
        pos = -1
        for i in range(len(arr)):
            if stack==[]:
                res.append(-1)
                stack.append(arr[i])
            else:
                while True:
                    if arr[i]>stack[-1]:
                        stack.pop()
                    if stack==[]:
                        res.append(-1)
                        stack.append(arr[i])
                        break
                    if arr[i]<stack[-1]:
                        res.append(stack[-1])
                        stack.append(arr[i])
                        break
        return res
if __name__== "__main__":
    arr = [1,3,2,4]
    print(solution().nextgreater(arr))
    print(solution().prevgreater(arr))
    # print(solution().nextgreatere1(arr))