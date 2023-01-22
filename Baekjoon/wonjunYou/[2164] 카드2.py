from collections import deque
import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

data = [i for i in range(1, n+1)]

q = deque(data)

while (len(q) > 1):
    q.popleft()
    q.append(q.popleft())

print(q[0])