class solution:
    def builds(self,n):
        oldb = 1
        olds = 1
        for i in range(2,n+1):
            newb = olds
            news = olds+oldb
            oldb = newb
            olds = news
        total = oldb+olds
        return total*total

if __name__ == "__main__":
    print(solution().builds(6))