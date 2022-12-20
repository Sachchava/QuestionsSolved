class solution:
    def findset(self,arr,ind,sett,summ,tar):
        if ind == len(arr)-1:
            if summ==tar:
                print(sett)
            return

        self.findset(arr,ind+1,sett+ " " + str(arr[ind]),summ+arr[ind],tar)
        self.findset(arr,ind+1,sett,summ,tar)
if __name__ == "__main__":
    arr = [70,10,20,30,40,50]  
    solution().findset(arr,0,"",0,70)