import sys


def dfs():
    global cache

    if len(cache) == M:
        print(*cache)
        return

    for num in array:
        if num not in cache:
            cache.append(num)
            dfs()
            cache.pop()


input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

cache = []
dfs()
