from queue import Queue 
  
# # function to find first non 
# # repeating character of sa Stream 
# def firstnonrepeating(Str):
#     global MAX_CHAR
#     q = Queue()
#     charCount = [0] * MAX_CHAR 
      
#     # traverse whole Stream
#     for i in range(len(Str)):
#         # push each character in queue 
#         q.put(Str[i]) 
#         # increment the frequency count 
#         charCount[ord(Str[i]) - ord('a')] += 1
#         # check for the non repeating
#         # character 
#         while (not q.empty()): 
#             if (charCount[ord(q.queue[0])-ord('a')] > 1): 
#                 q.get() 
#             else:
#                 print(q.queue[0], end = " ") 
#                 break
  
#         if (q.empty()): 
#             print(-1, end = " ")
#     print()
def firstnonrepeating1(s):
    dictt = dict()
    q = Queue()
    for i in range(len(s)):
        q.put(s[i])
        if s[i] not in dictt:
            dictt[s[i]]=1
        else:
            dictt[s[i]] = dictt.get(s[i],0)+1
        while not q.empty():
            if dictt[s[i]]>1:
                q.get()
            else:
                print(q.queue[0])
                break
        if q.empty():
            print(-1)

# Driver Code
MAX_CHAR = 26
Str = "aabc"
# firstnonrepeating(Str)
firstnonrepeating1(Str)