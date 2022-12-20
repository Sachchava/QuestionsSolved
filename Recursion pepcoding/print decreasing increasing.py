class solution:
    def pdi(self,n):
        if n==0:
            return
        print(n)
        self.pdi(n-1)
        print(n)
if __name__ == "__main__":
    solution().pdi(5)
