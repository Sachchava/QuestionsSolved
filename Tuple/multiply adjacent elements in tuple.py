t = (23,5,5,54,23)
l = len(t)
#for i in range(l-1):
    #print('answer is' + str(t[i]*t[i+1]))
a = tuple(map(lambda i,j:i*j,t[:-1],t[1:]))
print(a)    