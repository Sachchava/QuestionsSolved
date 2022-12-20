def isempty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
def pop(stack):
    if (isempty(stack)):
        print("underflow")
        return 
    return stack.pop(0)
def create():
    stack = []
    return stack
def reverse(stack):
    if not isempty(stack):
        ele = stack.pop(0)
        reverse(stack)
        push(stack,ele)

    
queue = [1,2,3,4]
print(queue)
reverse(queue)
print(queue)