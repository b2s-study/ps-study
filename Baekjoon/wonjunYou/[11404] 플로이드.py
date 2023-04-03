import sys

input = sys.stdin.readline

INF = float("inf")

N = int(input())
m = int(input())
bus = []

cost = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if i == j:
            cost[i][j] = 0

for i in range(m):
    a, b, c = map(int,sys.stdin.readline().rstrip().split())
    if cost[a][b] > c:
        cost[a][b] = c

for k in range(1, N + 1):
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            cost[i][j] = min(cost[i][j],cost[i][k] + cost[k][j])

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if cost[i][j] == INF:
            print(0, end=' ')
        else:
            print(cost[i][j],end=' ')
    print()