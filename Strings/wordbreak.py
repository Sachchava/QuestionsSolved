a = [ "leet","code" ]
b = "leetcode"
for i in range(len(b)):
    if b[i] in a:
        if b[i+1:] in a:
            print(True)
            break
