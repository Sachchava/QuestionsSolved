def aa(a,x):
    high = len(a)-1
    low = 0 

    while low <= high:
        mid = high + low//2
        if a[mid] > x:
            high = mid -1
        elif a[mid] < x:
            low = mid + 1 
        elif a[mid]==x:
            a1 = mid 
            high = mid-1  
    high = len(a)-1
    low = 0 
    while low <= high:
        mid = high + low//2
        if a[mid] > x:
            high = mid -1
        elif a[mid] < x:
            low = mid + 1 
        elif a[mid]==x:
            b = mid 
            low = mid+1   
    return a1,b
           
 
    
   

a = [1, 3, 5, 5, 5, 5, 67, 123, 125 ]
x = 67
print(aa(a,x))