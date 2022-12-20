class solution:
    def maxprofit(self,arr):
        obsp = -arr[0]
        ocsp = 0
        ossp = 0
        for i in range(1,len(arr)):
            if (ocsp-arr[i]>obsp):
                nbsp = ocsp-arr[i]
            else:
                nbsp = obsp
            if (obsp+arr[i]>ossp):
                nssp = obsp+arr[i]
            else:
                nssp = ossp
            if ocsp>ossp:
                ncsp = ocsp
            else:
                ncsp = ossp
            obsp = nbsp
            ossp = nssp
            ocsp = ncsp
        return ossp
if __name__ == "__main__":
    arr = [10,15,17,20,16,18,22,20,22,20,23,25]
    print(solution().maxprofit(arr))