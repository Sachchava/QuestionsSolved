s = "satitsh"
for i in range(len(s)-1):
    c = 1
    for j in range(i+1,len(s)):
        if s[i]==s[j]:
            c+=1
            print(s[i],c)
