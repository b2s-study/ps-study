import sys

input = sys.stdin.readline

def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()

n, m = map(int, input().rstrip('\n').split())
s = []

dfs(1)
