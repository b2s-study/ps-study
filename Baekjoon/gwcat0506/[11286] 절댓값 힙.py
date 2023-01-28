# https://www.acmicpc.net/problem/11286

# 우선순위 큐
# [절대값을 한 x, 원래원소] 형식으로 문제를 푼다.
# 그래서 우선순위 비교는 절대값을 한 x로 하고
# 출력은 원래 원소로 한다.

import sys
import heapq

N = int(sys.stdin.readline())

priory_heap = []
for _ in range(N):
    
    x = int(sys.stdin.readline())
    
    if x==0:
        if priory_heap:
            print(heapq.heappop(priory_heap)[1])
            continue
        print(0)
        continue
    
    heapq.heappush(priory_heap,[abs(x),x])
    
    # print(priory_heap)
