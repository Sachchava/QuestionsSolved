class solution:
    def fact(self,n):
        if n == 0:
            return 1
        return n*self.fact(n-1)
if __name__ == "__main__":
    print   (solution().fact(5))