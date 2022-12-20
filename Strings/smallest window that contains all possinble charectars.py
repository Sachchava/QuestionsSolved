a = "AABBBCBBAC"
b = ""
for i in range(len(a)):
    for j in range(i,len(a),3):
        b += a[j]
print(b)

