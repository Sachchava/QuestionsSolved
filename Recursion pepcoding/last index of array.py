class solution:
    def findxfl(self,arr,i):
        if i == len(arr):
            return -1
        ind = self.findxfl(arr,i+1)
        # if arr[i]==1:
        #     return i
        # else:
        #     return ind
        if ind ==-1:
            if arr[i]==1:
                return i
            else:
                return -1
        else:
            return ind
if __name__ == "__main__":
    arr = [2,6,23,4,3,1,4,5,34,67,854,4,564,2,1]
    print(solution().findxfl(arr,0))