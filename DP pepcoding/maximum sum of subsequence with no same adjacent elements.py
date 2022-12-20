class solution:
    def maxsum(self,arr):
        inc = arr[0]
        exc = 0
        for i in range(1,len(arr)):
            newinc = exc+arr[i]
            newexc = max(inc,exc)
            inc = newinc 
            exc = newexc
        return max(exc,inc)
if __name__ == "__main__":
    print(solution().maxsum([5,10,10,100,5,6]))