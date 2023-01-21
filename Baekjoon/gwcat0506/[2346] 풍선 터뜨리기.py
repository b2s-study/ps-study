# https://www.acmicpc.net/problem/2346

# deque 사용하기 

import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque(enumerate(map(int, input().split())))
# print(q)

result = []

while len(queue)>0:
    
    idx, next_num = queue.popleft()
    result.append(idx+1) # -> 풍선 번호는 idx에서 1더한 것 이므로

    # deque 회전시키기
    # 회전할 수가 양수이면 
    if next_num >= 0:
        queue.rotate(-(next_num-1))
    else:
        queue.rotate(-next_num)

print(*result)