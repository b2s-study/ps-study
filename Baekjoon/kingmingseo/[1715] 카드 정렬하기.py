import sys
import heapq

input = sys.stdin.readline
card = int(input())
min_heap = []
answer = 0

for i in range(card):
    card_count = int(input())
    heapq.heappush(min_heap, card_count)

while (len(min_heap) >1):
    temp1 = heapq.heappop(min_heap)
    temp2 = heapq.heappop(min_heap)
    answer = answer + temp1 + temp2
    heapq.heappush(min_heap , temp1 + temp2)



print(answer)




