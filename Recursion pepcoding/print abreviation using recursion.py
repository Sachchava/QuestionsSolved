class solution:
    def abbrev(self,strr,ans,count,ind):
        if ind == len(strr):
            if count==0:
                print(ans)
            else:
                print(ans+str(count))
            return 
        if count>0:
            self.abbrev(strr,ans+str(count)+strr[ind],0,ind+1)
        else:
            self.abbrev(strr,ans+strr[ind],count,ind+1)
        self.abbrev(strr,ans,count+1,ind+1)

if __name__ == "__main__":
    solution().abbrev("pep","",0,0)