import sys
from collections import deque

input = sys.stdin.readline

n = int(input().rstrip('\n'))

q = deque()

for i in range(1, n+1):
    q.append(i)

for i in range(n):
    if len(q) == 1:
        break

    q.popleft()
    q.rotate(-1)

print(*q)

