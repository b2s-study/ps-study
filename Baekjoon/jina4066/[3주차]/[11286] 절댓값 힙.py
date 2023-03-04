import sys
import heapq

input = sys.stdin.readline

N = int(input().rstrip('\n'))
heap = []

for _ in range(N):
    x = int(input().rstrip('\n'))

    if x != 0:
        heapq.heappush(heap, (abs(x), x))
    
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])


# import sys
# import heapq

# input = sys.stdin.readline

# q = []
# abs_heap = []
# count = 0


# N = int(input().rstrip('\n'))

# for _ in range(N):
#     x = int(input().rstrip('\n'))

#     if x != 0:
#         q.append(x)
#         q.sort()
#         heapq.heappush(abs_heap, abs(x))

#     else: 
#         if heapq.heappop(abs_heap) == abs_heap[0]: # 절댓값이 가장 작은 값이 여러개 일때,
#             for i in range(len(q)):
#                 if q[i] == abs_heap[0]:
#                     print(q[i])
#                     q.remove(q[i])
#                     break

                

            
