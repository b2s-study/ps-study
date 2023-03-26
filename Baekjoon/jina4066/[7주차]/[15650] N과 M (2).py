import sys

input = sys.stdin.readline

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        if visited[i] == True:
            continue
        # 만약 visited[i]가 False라면 방문처리
        visited[i] = True
        s.append(i)
        dfs(i + 1)
        s.pop()
        visited[i] = False

n, m = map(int, input().rstrip('\n').split())
s = []
visited = [False] * (n+1)

dfs(1)

