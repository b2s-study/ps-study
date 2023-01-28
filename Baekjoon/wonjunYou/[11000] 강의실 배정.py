import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip('\n'))

classes = []

for _ in range(n):
    classes.append(list(map(int, input().rstrip('\n').split())))

q = []
classes.sort()

heapq.heappush(q, classes[0][1])

for idx in range(1, n):

    if classes[idx][0] < q[0]:
        heapq.heappush(q, classes[idx][1])

    else:
        heapq.heappop(q)
        heapq.heappush(q, classes[idx][1])

print(len(q))