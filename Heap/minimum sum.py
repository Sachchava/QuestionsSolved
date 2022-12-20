from heapq import heappush,heappop
class solution:
    def summaker(self,arr):
        num1 = ""
        num2 = ""
        pq = []
        for i in range(len(arr)):
            heappush(pq,arr[i])
        i = 0
        print(pq)
        while i!=len(arr):
            ele1 = heappop(pq)
            if i%2==0:
                if ele1==0 and len(num1)==0:
                    i+=1
                    continue
                else:
                    i+=1
                    num1+=str(ele1)
            else:
                if ele1==0 and len(num2)==0:
                    i+=1
                    continue
                else:
                    i+=1
                    num2+=str(ele1)
        num1 = num1[::-1]
        num2 = num2[::-1]
        # print(num1,num2)
        if len(num1)>len(num2):
            num1,num2 = num2,num1
        carry = 0
        summ = 0
        ans = ""
        for i in range(len(num2)):
            summ = (ord(num1[i])-48)+(ord(num2[i])-48)+carry
            ans += chr(summ%10+48)
            carry = int(summ/10)
        for i in range(len(num1),len(num2)):
            summ = (ord(num2[i])-48)+carry
            ans += chr(summ%10+48)
            carry = int(summ/10)
        if carry:
            ans+=chr(carry+48)
        return ans[::-1]

if __name__ == "__main__":
    arr = [0,0,0, 5, 3, 0, 7, 4]
    s = solution()
    print(s.summaker(arr))