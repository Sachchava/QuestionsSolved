def aa(a,x):
    high = len(a)-1
    low = 0
    while low< high:
        mid = high+low//2
        if a[mid] ==x:
            return mid
        if a[low] < a[mid]:
            if x >= a[low] and a < a[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if x <= a[high] and x > a[mid]:
                low = mid +1
            else:
                high = mid-1
    return -1
a = [4,5,6,7,0,1,2]
x = 7
print(aa(a,x))