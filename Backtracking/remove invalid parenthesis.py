class solution:
    def getmin(self,str):
        stack = []
        for i in range(len(str)):
            if str[i] == "(":
                stack.append(str[i])
            else:
                if stack and stack[-1]=="(":
                    stack.pop()
                else:
                    stack.append(str[i])
        return len(stack)
    def remover(self,str,mr,s):
        if mr == 0:
            mrnow = self.getmin(str)
            if mrnow==0:
                s.add(str)
            return 
        for i in range(len(str)):
            left = str[:i]
            right = str[i+1:]
            self.remover(left+right,mr-1,s)
        return s
if __name__ == "__main__":
    str =  "()())()"
    mr = solution().getmin(str)
    s = set()
    print(solution().remover(str,mr,s))