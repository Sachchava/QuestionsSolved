class solution:
    def __init__(self):  
        self.st = []
        self.st2 = []
        self.input = []
        self.output = []
    def push(self,el):
        if self.st==[]:
            self.st.append(el)
        else:
            while self.st!=[]:
                remove = self.st.pop()
                self.st2.append(remove)
            self.st.append(el)
            while self.st2!=[]:
                aremove = self.st2.pop()
                self.st.append(aremove)
    def top(self):
        print(self.st[-1])
    def pop(self):
        print(self.st.pop())
    def push1(self,el):
        self.input.append(el)
    def pop1(self):
        if self.output == []:
            while self.input!=[]:
                remove = self.input.pop()
                self.output.append(remove)
            print(self.output.pop())
        else:
            print(self.output.pop())
    def top1(self):
        if self.output == []:
            while self.input!=[]:
                remove = self.input.pop()
                self.output.append(remove)
            print(self.output[-1])
        else:
            print(self.output[-1])
if __name__ == "__main__":
    s = solution()
    s.push(3)
    s.push(4)
    s.push(2)
    print(s.st)
    s.top()
    s.pop()
    s.top()

    print("=====")
    s.push1(3)
    s.push1(4)
    s.push1(2)

    s.top1()
    print(s.output)
    s.pop1()
    s.top1()


