class solution:
    def zigzag(self,n):
        if n==0:
            return
        print(n)
        self.zigzag(n-1)
        print(n)
        self.zigzag(n-1)
        print(n)
        # self.zigzag(self,n-1)
if __name__ == "__main__":
    n = 2
    solution().zigzag(n)