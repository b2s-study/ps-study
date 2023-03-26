import sys

input = sys.stdin.readline

def dfs(start):
    if len(s) == m:
        print(*s)
    for i in range(start, n):
        if lst[i] not in s:
            s.append(lst[i])
            dfs(i + 1)
            s.pop()

n, m = map(int, input().rstrip('\n').split())
lst = sorted(list(map(int, input().rstrip('\n').split())))
s = []

dfs(0)
