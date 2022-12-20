class solution:
    def count(self,strr):
        a,b,c = 0,0,0
        for e in strr:
            if e == "a":
                a = 2*a+1
            elif e == "b":
                b = 2*b+a
            elif e == "c":
                c = 2*c+b
        return c
if __name__ == "__main__":
    print(solution().count("abcabc"))