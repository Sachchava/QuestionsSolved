import string
import random
poss_char =  string.ascii_lowercase 
s = input('enter anything\n').lower()
i = 0
while s!=0:
    a = ''.join(random.choice(poss_char)for i in range(len(s)))
    print(a)
    i+=1
    if a==s:
        print(s)
        print('strings are matched after:' + str(i) + ' efforts')
        break

    