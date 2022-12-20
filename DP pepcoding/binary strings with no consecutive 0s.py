class solution:
    def noconz(self,n):
        oldz = 1
        oldo = 1
        for i in range(2,n+1):
            newz = oldo
            newo = oldo+oldz

            oldo = newo
            oldz = newz
        return oldo+oldz

if __name__ == "__main__":
    print(solution().noconz(6))