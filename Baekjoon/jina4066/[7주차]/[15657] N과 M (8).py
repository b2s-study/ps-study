import sys

input = sys.stdin.readline

def dfs(start):
    if len(s) == m:
        print(*s)
        return

    for i in range(start, n):
        s.append(lst[i])
        dfs(i)
        s.pop()

n, m = map(int, input().rstrip('\n').split())
lst = sorted(list(map(int, input().rstrip('\n').split())))
s = []

dfs(0)
