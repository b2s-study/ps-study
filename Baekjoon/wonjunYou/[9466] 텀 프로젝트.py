import sys

input = sys.stdin.readline

sys.setrecursionlimit(10**6)

def dfs(v):
    global result

    visited[v] = 1
    members.append(v)
    next_member = graph[v]

    if visited[next_member]:
        if next_member in members:
            result += members[members.index(next_member):]

            return
    else:
        dfs(next_member)

t = int(input().rstrip('\n'))

for _ in range(t):
    n = int(input().rstrip('\n'))

    visited = [0] * (n + 1)
    graph = [0] + list(map(int, input().rstrip('\n').split()))

    result = []
    for v in range(1, len(graph)):
        if not visited[v]:
            members = []
            dfs(v)

    print(n - len(result))