class solution:
    def evalprefix(self,s):
        res = []
        for i in range(len(s)-1,-1,-1):
            if s[i]>="0" and s[i]<="9":
                res.append(s[i])
            else:
                val2 = int(res.pop())
                val1 = int(res.pop())
                dictt = {"+":val1+val2,"-":val1-val2,"*":val1*val2,"/":val1/val2,"^":val1**val2}
                res.append(dictt.get(s[i]))
        return res.pop()
if __name__ == "__main__":
    s = "+9*26"
    print(solution().evalprefix(s))