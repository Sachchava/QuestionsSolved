class solution:
    def validate(self,pushed,popped):
        stack = []
        i = 0   
        for el in pushed:
            stack.append(el)
            while stack!=[] and stack[-1]==popped[i]:
                stack.pop()
                i+=1
        if stack==[]:
            return True
        return False


if __name__ == "__main__":
    pushed = [1, 2, 3]  
    popped = [2, 1, 3]
    print(solution().validate(pushed,popped))