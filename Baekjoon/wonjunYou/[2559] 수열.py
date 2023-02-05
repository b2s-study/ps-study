import sys

input = sys.stdin.readline

MIN_INF = -10000001

n, k = map(int, input().rstrip('\n').split())
temperatures = list(map(int, input().rstrip('\n').split()))

total = sum(temperatures[:k])
result = total

start, end = 0, k-1

for i in range(k, n):
    total += temperatures[i] - temperatures[i-k]
    result = max(result, total)

print(result)