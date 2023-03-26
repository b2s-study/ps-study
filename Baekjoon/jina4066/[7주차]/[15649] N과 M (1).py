import sys

input = sys.stdin.readline

def dfs(): 
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(1, n+1):
        if visited[i]:
            continue
        #visited[i] == false 일 경우 방문 처리
        visited[i] = True
        s.append(i)
        dfs()
        s.pop()
        visited[i] = False

n, m = map(int, input().rstrip('\n').split())
s = []
visited = [False] * (n+1)

dfs()