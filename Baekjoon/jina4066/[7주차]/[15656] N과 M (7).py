import sys

input = sys.stdin.readline

def dfs():
    if len(s) == m:
        print(*s)
        return

    for i in range(n):
        s.append(lst[i])
        dfs()
        s.pop()

n, m = map(int, input().rstrip('\n').split())
lst = sorted(list(map(int, input().rstrip('\n').split())))
s = []

dfs()
