class solution:
    def evalpost(self,s):
        stack = []
        for i in s:
            if i>="0" and i<="9":
                stack.append(i)
            else:
                # print(stack)
                val2 = int(stack.pop())
                print(val2)
                val1 = int(stack.pop())
                print(val1)
                dictt = {'+':val1+val2,'-':val1-val2,'*':val1*val2,'/':val1/val2,'^':val1**val2}
                stack.append(dictt.get(i))
                print("====")
        return stack
    def evalpost1(self,s):
        res = []
        for i in range(len(s)):
            if s[i]>='0' and s[i]<="9":
                res.append(s[i])
            else:
                val2 =int(res.pop())
                # print(val2)
                val1 = int(res.pop())
                # print(val1)
                dictt = {"+":val1+val2,"-":val1-val2,"*":val1*val2,"/":val1/val2,"^":val1**val2}
                res.append(dictt.get(s[i]))
        return res.pop()
if __name__ == "__main__":
    s = '583*+0-'
    # s = s.split(' ')
    print(s)
    print(solution().evalpost1(s))