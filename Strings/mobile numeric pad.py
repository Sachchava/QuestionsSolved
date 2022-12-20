a = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999" ]
b =   "Helo guys "
b = b.upper()
print("len is " + str(len(b)))
out = ""
for i in range(len(b)):
    if b[i]==" ":
        out = out + "0"
    else:
        p = ord(b[i])-ord("A")
        print(p)
        out = out + a[p]
print(out)