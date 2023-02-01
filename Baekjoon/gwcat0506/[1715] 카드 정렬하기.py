# https://www.acmicpc.net/problem/1715


# 1. 틀린풀이
# import sys
# import heapq

# N = int(sys.stdin.readline())

# heap = []
# for _ in range(N):
#     card_num = int(sys.stdin.readline())
#     heapq.heappush(heap,card_num)
    

# result = 0
# result+=(N-1)*heapq.heappop(heap)
# # print(result)

# for i in range(N-1):
#     print('i',i)
#     pop = heapq.heappop(heap)
#     result += (N-i-1)*pop
#     print('pop',pop)
#     # print(result)
    
# print(result)


# 위의 예외를 찾자면, 순서대로 작은수를 더하는 것이 아니라 앞에서 더하는 수는 반복이 되므로
# 반복되는 수를 최소화 해야한다. 
# 그래서 이전까지 더한 수 보다 새로운 수가 더 작으면 그 수로 앞으로 반복되는 수를 바꿔야 한다.
# 그래서 더하는 과정에서도 heap을 계속 이용한다. 

# 2. 정답풀이 -> 가장 작은수

import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    card_num = int(sys.stdin.readline())
    heapq.heappush(heap,card_num)
    

result = 0
# print(result)

while len(heap)>1:
    
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    sum_num = a+b
    result += sum_num
    heapq.heappush(heap,sum_num)
    
print(result)

