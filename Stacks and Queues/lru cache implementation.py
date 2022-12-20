from collections import OrderedDict
class lrucache:
    def __init__(self,n):
        self.size = n
        self.cache = OrderedDict()
    def get(self,key):
        if key not in self.cache:
            return -1
        else:
            self.cache.move_to_end(key)
            return self.cache[key]
    def put(self,key,value):
        self.cache[key]=value
        self.cache.move_to_end(key)
        if len(self.cache)>self.size:
            self.cache.popitem(last=False)
if __name__ == "__main__":
    cache = lrucache(3)
    cache.put(1, 1)
    print(cache.cache)
    cache.put(2, 2)
    print(cache.cache)
    cache.get(1)
    print(cache.cache)
    cache.put(3, 3)
    print(cache.cache)
    print("=====")
    cache.get(2)
    print(cache.cache)
    cache.put(4, 4)
    print(cache.cache)
    cache.get(1)
    print(cache.cache)
    cache.get(3)
    print(cache.cache)
    cache.get(4)
    print(cache.cache)