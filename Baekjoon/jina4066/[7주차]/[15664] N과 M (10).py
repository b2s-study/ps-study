import sys

input = sys.stdin.readline

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    idx = 0

    for i in range(start, n):
        if visited[i] == False and idx != lst[i]:
            visited[i] = True
            s.append(lst[i])
            idx = lst[i]
            dfs(i+1)
            visited[i] = False
            s.pop()

n, m = map(int, input().rstrip('\n').split())
lst = sorted(list(map(int, input().rstrip('\n').split())))
s = []
visited = [False] * n

dfs(0)
