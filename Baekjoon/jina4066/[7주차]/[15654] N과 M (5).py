import sys

input = sys.stdin.readline

def dfs(depth):
    if depth == m : 
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if visited[i] == True:
            continue

        visited[i] = True
        s.append(lst[i])
        dfs(depth + 1)
        s.pop()
        visited[i] = False

n, m = map(int, input().rstrip('\n').split())
lst = sorted(list(map(int, input().rstrip('\n').split())))
s = []
visited = [False] * n

dfs(0)
