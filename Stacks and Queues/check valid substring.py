class solution:
     
 
    def check(self,s):
        left = right = 0
        validcount = 0
        for i in range(len(s)):
            if s[i]=="(":
                left+=1
            else:
                right+=1
            if left==right:
                if left>validcount:
                    validcount = left*2
            if right>left:
                right = left = 0
        right = left = 0
        for i in range(len(s)-1,-1,-1):
            if s[i]=="(":
                left+=1
            else:
                right+=1
            if left==right:
                if right>validcount:
                    validcount = right*2
            elif left>right:
                left = right = 0
        return validcount
    def substring(self,s):
        res = []
        for i in range(len(s)):
            sub = ""
            for j in range(i,len(s)):
                sub+=s[j]
                res.append(sub)
        return res
    def validsubpar(self,s):
        stack = []
        for i in range(len(s)):
            if s[i] in ["(","[","{"]:
                stack.append(s[i])
            else:
                if stack==[]:
                    return False
                char = stack.pop()
                if char=="(":
                    if s[i]==")":
                        return True
        if stack:
            return False
        return True
    def validcheck(self,s):
        maxvalid = 0
        for i in s:
            if self.validsubpar(i):
                maxvalid = max(maxvalid,len(i))
        return maxvalid

    
if __name__== "__main__":
    s = "()(())("
    # print(solution().check(s))
    print("====")
    string = solution().substring(s)
    print(string)
    print(solution().validcheck(string))