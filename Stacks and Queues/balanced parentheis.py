class solution:
    def checkbalance(self,s):
        stack = []
        
        for i in range(len(s)):
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
         
            else:
                if stack==[]:
                    return False
                char = stack.pop()
                if char =="(":
                    if s[i]!=")":
                        return False
                # elif stack==[]:
                    # return False
                elif char =="[":
                    if s[i]!="]":
                        return False
                elif char =="{":
                    if s[i]!="}": 
                        return False
        if stack:
            return False
        return True
if __name__ == "__main__":
    s = ")))"
    print( solution().checkbalance(s))