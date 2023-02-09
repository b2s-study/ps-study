import sys
from collections import deque


def is_out_of_range(index):
    return (index < 0 or index >= MAX_LENGTH)


def bfs(start):
    visited[start] = True
    time_list[start] = 0

    q = deque()
    q.append(start)
    while (q):
        X = q.popleft()
        if X == K:
            break

        for next in [X-1, X+1, X*2]:
            if is_out_of_range(next) or visited[next]:
                continue
            q.append(next)
            visited[next] = True
            time_list[next] = time_list[X] + 1

    return time_list[K]


input = sys.stdin.readline

N, K = map(int, input().split())
MAX_LENGTH = 200002
time_list = [0] * MAX_LENGTH
visited = [False] * MAX_LENGTH

min_time = bfs(N)
print(min_time)
