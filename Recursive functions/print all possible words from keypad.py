def k(s,a):
    if len(s)==0:
        print(a)
        return
    h = ["", "", "abc", "def", "ghi", "jkl",
             "mno", "pqrs", "tuv", "wxyz"]
    c = s[0]
    code = int(h(c))
    r = s[1:]
    for i in range(len(code)):
        k(r ,a+code[i])
k("23","")