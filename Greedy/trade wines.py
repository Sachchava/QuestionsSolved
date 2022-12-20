class solution:
    def minwork(self):
        n = int(input("size of array"))
        arr = []
        for i in range(n):
            arr.append(int(input("array elements")))
        buyer = []
        seller = []
        for i in range(n):
            if arr[i]<0:
                seller.append([arr[i],i])
            else:
                buyer.append([arr[i],i])
        i = 0
        j = 0
        work = 0
        print(buyer,seller)
        while i<len(buyer) and j< len(seller):
            minv = min(buyer[i][0],-seller[j][0])
            buyer[i][0]+=-minv
            seller[j][0]+=minv
            distance = abs(buyer[i][1]-seller[j][1])
            work+=distance*minv
            if buyer[i][0]==0:
                i+=1
            if seller[j][0]==0:
                j+=1
        return work


        
if __name__ == "__main__":
    print(solution().minwork())