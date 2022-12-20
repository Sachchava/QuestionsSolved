#josephus problem
class solution:
    def josephus(self,n,k):
        if n==1:
            return 0
        x = self.josephus(n-1,k)
        y = (x+k)%n
        return y
if __name__ == "__main__":
    print(solution().josephus(5,2))