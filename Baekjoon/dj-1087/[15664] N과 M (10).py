import sys


def dfs(idx=-1):
    global idx_case, sub_array_set

    if len(idx_case) == M:
        result = []
        for i in idx_case:
            result.append(array[i])
        sub_array_set.add(tuple(result))
        return

    for i in range(idx+1, N):
        idx_case.append(i)
        dfs(i)
        idx_case.pop()


input = sys.stdin.readline

N, M = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

idx_case = list()
sub_array_set = set()
dfs()

result = list(sub_array_set)
result.sort()
for each in result:
    print(*each)
