class Students:
    def __init__(self,m1,m2):
        self.m1 = m1 
        self.m2 = m2

    def __add__(self,other):
        
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        a = Students(m1,m2)
        return a
    
    def __sub__(self,other):
        
        m1 = self.m1 - other.m1
        m2 = self.m2 - other.m2
        a = Students(m1,m2)
        return a

    def __mul__(self,other):
        m1 = self.m1 * other.m1
        m2 = self.m2 * other.m2
        a = Students(m1,m2)
        return a
    
    def __gt__(self,other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        if m1 > m2:
            return True
        else:
            return False 
    
    def __str__(self):
        return '{} {} '.format (self.m1 , self.m2)

s1 = Students(23,914)
s2 = Students(564,22)
s3 = s1 + s2
print(s3.m1)
s3 = s2 - s1
print(s3.m2)        
s3 = s1 * s2
print(s3.m1)
if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')
print(s1)