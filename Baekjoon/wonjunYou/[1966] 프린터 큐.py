from collections import deque
import sys

input = sys.stdin.readline

t = int(input().rstrip('\n'))

for _ in range(t):
    n, m = map(int, input().rstrip('\n').split())
    priorities = list(map(int, input().rstrip('\n').split()))

    q = deque(priorities)

    order = 0

    while (m > -1):
        if q[0] == max(q):
            q.popleft()
            m -= 1
            order += 1

        else:
            q.append(q.popleft())

            if m == 0:
                m = len(q) - 1
            else:
                m -= 1
    print(order)






