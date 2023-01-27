import heapq
import sys
input = sys.stdin.readline

max_heap = []
temp = []

count = int(input())

for _ in range(count):
    temp.append(int(input()))

for i in temp:
    if i == 0:
        if len(max_heap) == 0 :
            print("0")
        else :
            print(heapq.heappop(max_heap) * -1)

    else :
        heapq.heappush(max_heap, i * -1)


