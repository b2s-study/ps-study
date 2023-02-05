import sys

input = sys.stdin.readline

N, K = map(int, input().split())
array = list(map(int, input().split()))

start = 0
max_sum = sum(array[start:start+K])
current_sum = sum(array[start:start+K])
while (True):
    if start+K >= len(array):
        break

    current_sum = current_sum - array[start] + array[start+K]
    max_sum = max(max_sum, current_sum)
    start += 1

print(max_sum)
