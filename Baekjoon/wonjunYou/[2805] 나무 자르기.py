import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

woods = list(map(int, input().rstrip('\n').split()))

start = 0
end = max(woods)

result = 0
while (start <= end):
    total = 0

    mid = (start + end) // 2

    for idx in range(len(woods)):
        if woods[idx] > mid:
            total += (woods[idx] - mid)

    if total < m:
        end = mid - 1

    else:
        result = mid
        start = mid + 1

print(result)