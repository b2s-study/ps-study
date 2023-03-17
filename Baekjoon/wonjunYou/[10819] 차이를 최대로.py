import sys

def dfs(depth, total, prev):
    global result

    if depth == n:
        result = max(result, total)
        return

    for idx in range(n):
        if not isused[idx]:
            isused[idx] = 1

            if depth > 0:
                total += abs(prev - numbers[idx])

            prev = numbers[idx]

            dfs(depth + 1, total, prev)

            if depth > 0:
                total -= abs(prev - numbers[idx])

            isused[idx] = 0


input = sys.stdin.readline

n = int(input().rstrip('\n'))
numbers = list(map(int, input().rstrip('\n').split()))

isused = [0] * n

result = 0

dfs(0, 0, 0)
print(result)
