class solution:
    def findways(self,x):
        if x==0:
            return [""]
        if x<0:
            return []
        path1 = self.findways(x-1)
        path2 = self.findways(x-2)
        path3 = self.findways(x-3)
        ans = []
        for e in path1:
            ans.append(e+"1")
        for e in path2:
            ans.append(e+"2")
        for e in path3:
            ans.append(e+"3")
        return ans

if __name__ == "__main__":
    x = 4
    print(solution().findways(x))