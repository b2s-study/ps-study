# https://www.acmicpc.net/problem/11000

# 겁나 어렵다..

# import sys
# import heapq

# N = int(sys.stdin.readline())


# l = []
# for _ in range(N):
    
#     s,t = map(int,sys.stdin.readline().split())
#     l.append([s,t])
# # 미리 한 번 정렬해준다. 
# l.sort()
# # print(l)
# # l = [[1, 3], [2, 4], [3, 5]]
# # heap = [[1, 3]]
# heap = []
# for i in range(N):
    
#     if len(heap)==0:
#         heapq.heappush(heap,l[i])
#         # print(heap)
#         continue
    
#     # 현재 회의 끝나는 시간(heap[0][1])과 새로 push(l[i][0])할 회의 시작시간 비교 
#     if heap > l[i][0]:
#         heapq.heappush(heap,l[i]) 
#         # print(heap)
#     # 회의시간이 겹치지 않으면 회의 합쳐서 다시 push  
#     else:
#         sum_time = heapq.heappop(heap)
#         a,b = sum_time[0],l[i][1]
#         heapq.heappush(heap,[a,b]) 
#         # print(heap)      
# print(len(heap))
    
    
# 풀이 2. 
import heapq
import sys

N = int(sys.stdin.readline())

q = []

for i in range(N):
    s, t = map(int, sys.stdin.readline().split())
    q.append([s, t])

q.sort()
room = []
heapq.heappush(room, q[0][1])

for i in range(1, N):
    
    if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
        heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
    else: # 현재 회의실에 이어서 회의 개최 가능
        heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
        heapq.heappush(room, q[i][1])
# print(room)
print(len(room))
