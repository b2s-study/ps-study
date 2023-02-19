import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        current = q.popleft()

        if current == K:
            return points[current]

        for next in [current*2, current-1, current+1]:
            if (0 <= next < MAX_LENGTH) and not visited[next]:
                time = points[current]
                if next == current*2:
                    q.appendleft(next)
                else:
                    q.append(next)
                    time += 1

                points[next] = time
                visited[next] = True

    return -1


input = sys.stdin.readline

N, K = map(int, input().split())
MAX_LENGTH = 100001
points = [0] * MAX_LENGTH
visited = [False] * MAX_LENGTH
time = bfs(N)
print(time)
