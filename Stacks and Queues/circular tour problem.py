class trip:
    def __init__(self,a,b):
        self.petrol = a
        self.distance = b
class solution:
    def circlecheck(self,arr):
        fueltank = 0
        deficietfuel = 0
        start = 0
        for i in range(len(arr)):
            fueltank += arr[i].petrol - arr[i].distance
            if fueltank <0:
                start = i+1
                deficietfuel = fueltank
                fueltank = 0
        if fueltank+deficietfuel>=0:
            return start
        return -1
if __name__ == "__main__":
    arr = [trip(4,6),trip(6,5),trip(7,3),trip(4,5)]
    print(solution().circlecheck(arr))