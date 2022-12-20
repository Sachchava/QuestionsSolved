from difflib import *
def closeststring(s,m):
    return get_close_matches(s,m)
s = 'appel'
m = ['apple','ape','aapse','aap','aaple','appo']    
print(closeststring(s,m))