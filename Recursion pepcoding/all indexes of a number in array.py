class solution:
    def allind(self,arr,ans,i):
        if arr[i]==3:
            ans.append(i)
        if i == len(arr)-1:
            return 
        self.allind(arr,ans,i+1)
        return ans
if __name__=="__main__":
    arr = [23,43,3,65,23,4,3,12,4,23,534,3]
    o = solution().allind(arr,[],0)
    print(o)