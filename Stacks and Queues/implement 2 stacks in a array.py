class twostacks:
    def __init__(self,n):
        self.size = n
        self.top = -1
        self.arr = [None]*n
        self.end = self.size
    def push1(self,x):
        if self.top<self.end-1:
            self.top = self.top+1
            self.arr[self.top] = x
        else:
            print("overflow")
            return
    def push2(self,x):
        if self.top<self.end-1:
            self.end = self.end-1
            self.arr[self.end] = x
        else:
            print("overflow2")
            return
    def pop1(self):
        if self.top>=0:
            x = self.arr[self.top]
            self.top = self.top-1
            return x
        else:
            print("underflow")
            return 
    def pop2(self):
        if self.end<self.size-1:
            x = self.arr[self.end]
            self.end = self.end+1
            return x
        else:
            print("underflow")
            return 
    def printer(self):
        print(self.arr)
if __name__=="__main__":
    t = twostacks(5)
    t.push1(1)
    t.push2(5)
    t.push2(4)
    t.push2(3)
    t.push1(2)
    print(t.pop1())
    print(t.pop2())
    t.printer()