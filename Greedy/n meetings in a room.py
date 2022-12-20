class solution:
    def pairs(self,arr1,arr2):
        arr = []
        for i in range(len(arr1)):
            arr.append((arr1[i],arr2[i]))
        return arr
    def count(self,arr):
        i = 0
        j = 1
   
        while i!=len(arr)-1 and j!=len(arr):
            if arr[i][1]<arr[j][0]:
                i+=1
                j+=1
            elif arr[i][1]>=arr[j][0]:
                arr.pop(j)
            if len(arr)==1:
                break
            if arr == []:
                return 1
        return len(arr),arr

if __name__ == '__main__':
    a1 = [ 10, 12, 20]
    a = [20, 25, 30 ]
    aa = solution().pairs(a1,a)
    ab=(sorted(aa,key = lambda x:x[1]))
    # abb=(sorted(aa,key = lambda x:x[0]))
    print(ab)
    print(solution().count(ab))