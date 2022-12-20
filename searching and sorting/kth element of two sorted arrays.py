class Solution:
    def aa(a,b,n,m,k):
        def bb(a,b,n,m,num):
            c = 0
            low , high=0,n-1
            while low<=high:
                mid = (low+high )//2
                if a[mid]<=num:
                    low = mid+1
                else:
                    high = mid-1
            c+=low
            low ,high = 0,m-1
            while low<=high:
                if b[mid]<=num:
                    low=mid+1
                else:
                    high = mid-1
            c+=low
            return c
        low = min(a[0],b[0])
        high = max(a[-1],b[-1])
        while low<=high:
            mid = (low+high)//2
            if bb(a,b,n,m,mid)<k:
                low = mid+1
            else:
                high = mid -1
        return low
def main():

    T = int(input())

    while(T > 0):
        sz = [int(x) for x in input().strip().split()]
        n, m, k = sz[0], sz[1], sz[2]
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement( a, b, n, m, k))

        T -= 1


if __name__ == "__main__":
    main()