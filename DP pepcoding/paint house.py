class solution:
    def mincost(self,arr):
        r = arr[0][0]
        b = arr[0][1]
        g = arr[0][2]
        for i  in range(1,len(arr)):
            nr = min(b,g) + arr[i][0]
            nb = min(r,g) + arr[i][1]
            ng = min(r,b) + arr[i][2]
            r = nr
            b = nb
            g = ng
        return min(r,g,b)
if __name__ == "__main__":
    arr = [[1, 2, 3],[11, 14, 5],[14, 3, 10]]
    print(solution().mincost(arr))