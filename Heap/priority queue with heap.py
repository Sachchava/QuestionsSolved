# h = [0]*10
# size = 0
# def parent(i):
#     return int(i-1/2)
# def shiftUp(i):
#     while i>=0 and h[parent(i)]<h[i]:
#         h[parent(i)],h[i] = h[i],h[parent(i)]
#         i = parent(i)
# def shiftDown(i):
#     largest = i
#     left = (2*i)+1
#     right = (2*i)+2
#     if left<size and h[left]>h[largest]:
#         largest = left
#     if right<size and h[right]>h[largest]:
#         largest = right
#     if largest!=i:
#         h[largest],h[i] = h[i],h[largest]
#         shiftDown(largest)  
# def extractMax():
#     global size
#     result = h[0]
#     h[0] = h[size]
#     size=size-1
#     shiftDown(0)
#     return result
# def insert(i):
#     global size
#     h[size] = i
#     size+=1
#     shiftUp(size)
# def changePriority(i,val):
#     oldp = h[i]
#     h[i] = val
#     if val>oldp:
#         shiftUp(i)
#     else:
#         shiftDown(i)
# insert(45)
# insert(20)
# insert(14)
# insert(12)
# insert(31)
# insert(7)
# insert(11)
# insert(13)
# insert(7)
# i = 0
# # print(size)
# # Priority queue before extracting max
# print("Priority Queue : ", end = "")
# while (i < size) :
 
#     print(h[i], end = " ")
#     i += 1
   
# print()
# print("Node with maximum priority :" ,  extractMax())
# # print(size)
# print("Priority queue after extracting maximum : ", end = " ")
# j = 0
# print(h)
# while (j <= size) :
#     print(h[j], end = " ")
#     j += 1
# print()
# changePriority(2, 49)
# print("Priority queue after priority change : ", end = "")
# k = 0
# while (k <= size) :
 
#     print(h[k], end = " ")
#     k += 1
   
# print()
 