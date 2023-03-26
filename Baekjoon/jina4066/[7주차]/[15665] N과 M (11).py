import sys

input = sys.stdin.readline

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    idx = 0

    for i in range(n):
        if idx != lst[i]:
            visited[i] = True
            s.append(lst[i])
            idx = lst[i]
            dfs()
            visited[i] = False
            s.pop()

n, m = map(int, input().rstrip('\n').split())
lst = sorted(list(map(int, input().rstrip('\n').split())))
s = []
visited = [False] * n

dfs()
