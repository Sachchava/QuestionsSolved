class solution:
    def pairing(self,i,n,used,asf):
        if i > n:
            print(asf)
            return
        if used[i]==True:
            self.pairing(i+1,n,used,asf)
        else:
            used[i] = True
            self.pairing(i+1,n,used,asf+ "(" + str(i)+ ")")
            for j in range(i+1,n+1):
                if used[j]==False:
                    used[j] = True
                    self.pairing(i+1,n,used,asf + "(" + str(i) + str(j) + ")")
                    used[j]= False
                    
            used[i] = False
if __name__ == "__main__":
    n = 3
    used = [False for i in range(n+1)]
    asf = ""
    solution().pairing(1,n,used,asf)