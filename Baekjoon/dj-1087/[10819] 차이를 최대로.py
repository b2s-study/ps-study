import sys


def dfs(idx, value):
    global N, array, used, step, max_val
    if step == N-1:
        max_val = max(max_val, value)
        return

    current_val = array[idx]
    for i in range(N):
        if not used[i]:
            next_val = array[i]
            new_val = value + abs(current_val - next_val)
            used[i] = True
            step += 1

            dfs(i, new_val)

            used[i] = False
            step -= 1


# dfs롤 숫자 1개씩 탐색
# 모든 숫자 탐색 후 최댓값 갱신
input = sys.stdin.readline

N = int(input())
array = list(map(int, input().split()))

used = [False] * N
step = 0
max_val = -1*sys.maxsize
for i in range(N):
    used[i] = True
    dfs(i, 0)
    used[i] = False

print(max_val)
