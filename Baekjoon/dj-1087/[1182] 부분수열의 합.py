import sys


def dfs(idx=-1):
    global S, array, sum_val, count
    if sum_val == S and idx != -1:
        count += 1

    for i in range(idx+1, N):
        sum_val += array[i]
        dfs(i)
        sum_val -= array[i]


input = sys.stdin.readline

N, S = map(int, input().split())
array = list(map(int, input().split()))

count = 0
sum_val = 0
dfs()

print(count)
