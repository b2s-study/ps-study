# https://www.acmicpc.net/problem/2164


# 풀이1. 시간 초과 ...
# import sys
# N = int(sys.stdin.readline())

# # 카드 리스트 만들기
# N_list = list(range(1,N+1))   
# # print(N_list)
    
# while len(N_list)!=1:
    
#     # 젤 위 버리기
#     N_list.pop(0)
#     # print('1',N_list)
#     # 그 다음을 아래로 옮기기
#     N_list.append(N_list.pop(0))
    
#     # print('2',N_list)
    
# print(N_list.pop(0))
    
    
    
# 풀이2. 덱을 이용 

from collections import deque
import sys
N = int(sys.stdin.readline())


# 카드 리스트 만들기
N_list = list(range(1,N+1))   

queue = deque()
queue.extend(N_list)

while len(queue)!=1:
    
    # 1. 젤 위 버리기
    queue.popleft()
    # print('1',queue)
    
    # 2. 그 다음을 아래로 옮기기 -> 덱에서 로테이션 시키기 
    queue.rotate(-1)
    # print('2',queue)

print(queue.popleft())