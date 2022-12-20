class solution:
    def maxsum(self,s1,s2,s3):
        sum1 = sum(s1)
        sum2 = sum(s2)
        sum3 = sum(s3)
        while True:
            if sum1==sum2 and sum2 == sum3:
                return sum1
            if s1 ==[] or s2 == [] or s3 == []:
                return 0
            t1 = 0
            t2 = 0
            t3 = 0
            if sum1>=sum2 and sum1>=sum3:
                sum1-=s1[t1]
                t1+=1
            elif sum2>=sum1 and sum2>=sum3:
                sum2-=s2[t2]
                t2+=1
            elif sum3>=sum1 and sum3>=sum2:
                sum3-=s3[t3]
                t3+=1


if __name__ == "__main__":
    s1 = [ 3, 2, 1, 1, 1 ]
    s2 = [4, 3, 2 ]
    s3 = [1, 1, 4, 1]
    print(solution().maxsum(s1,s2,s3))