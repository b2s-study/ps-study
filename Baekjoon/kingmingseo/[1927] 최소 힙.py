import heapq
import sys
input = sys.stdin.readline

min_heap = []
temp = []

count = int(input())

for _ in range(count):
    temp.append(int(input()))


for i in temp:
    if i == 0:
        if len(min_heap) == 0 :
            print("0")
        else :
            print(heapq.heappop(min_heap ))

    else :
        heapq.heappush(min_heap, i )


