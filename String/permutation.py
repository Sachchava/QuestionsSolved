from itertools import permutations
def permutation(s):
    p = permutations(s)
    for i in p:
        print(''.join(i),i)
s = 'abcd'
permutation(s)        