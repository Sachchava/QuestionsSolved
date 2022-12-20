class solution:
    def maxprofit(self,arr,fee):
        obsp = -arr[0]
        ossp = 0
        for i in range(len(arr)):
            if (ossp-arr[i]>obsp):
                nbsp = ossp-arr[i]
            else:
                nbsp = obsp
            if (nbsp+arr[i]-fee>ossp):
                nssp = nbsp+arr[i]-fee
            else:
                nssp = ossp
            obsp = nbsp
            ossp = nssp
        return ossp
if __name__ == "__main__":
    arr = [10,15,17,20,16,18,22,20,22,20,23,25]
    fees = 3
    print(solution().maxprofit(arr,fees))