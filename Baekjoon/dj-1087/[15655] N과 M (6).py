import sys


def dfs(idx=-1):
    global cache

    if len(cache) == M:
        print(*cache)
        return

    for i in range(idx+1, len(array)):
        cache.append(array[i])
        dfs(i)
        cache.pop()


input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

cache = []
dfs()
