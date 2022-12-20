class solution:
    def arranger(self):
        t = int(input("test cases \n"))
        while t!=0:
            n = int(input("len of amplifiers array"))
            arr = []
            ones = 0
            for i in range(n):
                e = int(input("array elements \n"))
                arr.append(e)
                if arr[i]==1:
                    ones +=1
            arr.sort(reverse = True)
            for i in range(ones):
                print('1',end = '')
            if n-ones == 2 and arr[0]==3 and arr[1] == 2:
                print("23",end = "")
            else:
                for i in range(n-ones):
                    print(arr[i],end = '')
                
            t-=1

if __name__ == "__main__":
    solution().arranger()