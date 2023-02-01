# https://www.acmicpc.net/problem/11279

import sys
import heapq

N = int(sys.stdin.readline())

heap = []
for _ in range(N):
    
    x = int(sys.stdin.readline())
    
    if x==0:
        if len(heap)==0:
            print(0)
            continue
        print(-heapq.heappop(heap))
        continue
    heapq.heappush(heap,-x)