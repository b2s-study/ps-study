import sys

input = sys.stdin.readline

def func(lens):

    if lens == m:
        print(*answer)
        return

    for idx in range(1, n + 1):
        if not visited[idx]:
            visited[idx] = 1
            answer[lens] = idx
            func(lens + 1)
            visited[idx] = 0

n, m = map(int, input().rstrip('\n').split())

answer = [0] * m
visited = [0] * (n + 1)

func(0)