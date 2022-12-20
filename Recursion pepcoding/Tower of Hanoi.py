class solution:
    def toh(self,n,t1,t2,t3):
        if n==0:
            return 
        self.toh(n-1,t1,t3,t2)
        print(str(n)+"["+str(t1)+"-> "+str(t2)+"]")
        self.toh(n-1,t3,t2,t1)
    def TowerOfHanoi(self,n , from_rod, to_rod, aux_rod):
        if n == 0:
            return
        self.TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
        print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
        self.TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
if __name__ =="__main__":
    n = 4
    solution().toh(n,"A","B","C")
    # solution().TowerOfHanoi(n,"A","B","C")