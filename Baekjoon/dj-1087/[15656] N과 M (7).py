import sys


def dfs():
    global cache

    if len(cache) == M:
        print(*cache)
        return

    for i in range(len(array)):
        cache.append(array[i])
        dfs()
        cache.pop()


input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

cache = []
dfs()
