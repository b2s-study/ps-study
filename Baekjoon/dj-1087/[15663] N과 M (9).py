import sys


def dfs():
    global idx_case, sub_array_set

    if len(idx_case) == M:
        result = []
        for i in idx_case:
            result.append(array[i])
        sub_array_set.add(tuple(result))
        return

    for i in range(0, N):
        if i not in idx_case:
            idx_case.append(i)
            dfs()
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
