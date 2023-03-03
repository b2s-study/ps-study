import sys


def dfs(current=0):
    global array

    if len(array) == M:
        print(*array)
        return

    for i in range(1, N+1):
        if i > current:
            array.append(i)
            dfs(i)
            array.pop()


N, M = map(int, input().split())
array = []

dfs()
