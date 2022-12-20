class solution:
    def findkingdom(self):
        width = int(input("width"))
        height = int(input("height"))
        towers = int(input("towers"))
        xcord = [0]
        ycord = [0]
        for i in range(towers):
            xcord.append(int(input("x cordinate")))
            ycord.append(int(input("y cordinate")))
        xcord.append(width+1)
        ycord.append(height+1)
        xcord.sort()
        ycord.sort()
        maxx = 0
        maxy = 0
        print(xcord,ycord)
        for i in range(len(xcord)-1):
            if xcord[i+1]-xcord[i]-1>maxx:
                maxx = xcord[i+1]-xcord[i]-1
            if ycord[i+1]-ycord[i]-1>maxy:
                maxy = ycord[i+1]-ycord[i]-1
        return maxx,maxy,maxx*maxy


if __name__ == "__main__":
    print(solution().findkingdom())