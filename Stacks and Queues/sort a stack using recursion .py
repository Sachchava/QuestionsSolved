def sortstack(stack):
    if len(stack)!=0:
        data = stack.pop()
        sortstack(stack)
        insertsorted(stack,data)
def insertsorted(stack,data):
    if len(stack)==0 or data>s[-1]:
        stack.append(data)
        return 
    else:
        ele = stack.pop()
        insertsorted(stack,data)
        stack.append(ele)

s = [ ]
s.append(30)
s.append(-5)
s.append(18)
s.append(14)
s.append(-3)
print(s)
sortstack(s)
print(s)