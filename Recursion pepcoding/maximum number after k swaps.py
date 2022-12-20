class solution:
    def swaps(self,str,k,maxstr):
        if str>maxstr:
            maxstr = str
        if k == 0:
            return 
        n = len(str)
        for i in range(n):
            for j in range(i+1,n):
                if str[i]<str[j]:
                    swapped = self.swap(str,i,j)
                    self.swaps(swapped,k-1,swapped)
        return maxstr
    def swap(self,str,i,j):
        left = str[:i]
        ith = str[i]
        mid = str[i+1:j]
        jth = str[j]
        right = str[j+1:]
        return left+jth+mid+ith+right

if __name__ == "__main__":
    print(solution().swaps("1234567",4,"1234567"))