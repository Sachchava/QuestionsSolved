def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
def pop(stack):
    if (isempty(stack)):
        print("underflow")
        return 
    return stack.pop()
def create():
    stack = []
    return stack
def reverse(stack):
    if not isempty(stack):
        ele = stack.pop()
        reverse(stack)
        insertAtBottom(stack,ele)
def insertAtBottom(stack, item):
    if isempty(stack):
        push(stack,item)
    else:
        temp = pop(stack)
        insertAtBottom(stack, item)
        push(stack, temp)
def reversee(stack,i):
    # print(i)
    if i == -len(stack)-1:
        return 
    data = stack.pop(i)
    stack.append(data)
    i-=1
    reversee(stack,i)
   
    return stack
stack = [4,3,2,1]
print(stack)
reversee(stack,-2)
print(stack)
reverse(stack)
print(stack)