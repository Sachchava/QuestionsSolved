a = [30,40,50,10,20]
# a = [50,10,20,30,40]
# a = [40,50,10,20,30]
def m(a):
    low = 0
    high = len(a)-1
    while low < high:
        mid = int((low+high)//2)
        if a[mid] < a[low] :
            high = mid -1
        if a[mid]> a[mid+1]:
            return a[mid+1]   
        if a[mid] < a[mid-1]:
            return a[mid]
               

    low1 = 0
    high1 = len(a)-1

    while low1 < high1:
        mid = int((low1+high1)//2)
        if a[mid] > a[high1] :
            low1 = mid +1
        if a[mid]> a[mid+1]:
            return a[mid+1]                
    # low2 = 0
    # high2 = len(a)-1

    # while low2 < high2:
    #     mid= int((low2+high2)//2)
    #     if a[mid] < a[mid-1]:
    #         return a[mid]              
print(m(a))