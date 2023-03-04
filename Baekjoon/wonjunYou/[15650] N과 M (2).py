import sys

input = sys.stdin.readline

def func(lens):
    if lens == m:
        print(*result)
        return

    for idx in range(1, n+1):
        if not visited[idx]:
            if lens > 0 and result[lens - 1] > idx:
                continue

            result[lens] = idx
            visited[idx] = 1
            func(lens + 1)
            visited[idx] = 0

n, m = map(int, input().rstrip('\n').split())

result = [0] * m
visited = [0] * (n + 1)

func(0)