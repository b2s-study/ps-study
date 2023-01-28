import sys
import heapq
from queue import PriorityQueue

input = sys.stdin.readline
loop = int(input())

q = PriorityQueue()
answer = 1
end_list = []

for i in range(loop):
    start, end = map(int,input().split())
    q.put((start , end))

value = q.get()
heapq.heappush(end_list, value[1])


while (q.qsize() > 0) :
    value = q.get()
    start = value[0]
    end = value[1]
    if  start< end_list[0] :
        answer = answer +1
        heapq.heappush(end_list, end)
    else :
        heapq.heappop(end_list)
        heapq.heappush(end_list, end)

print(answer)