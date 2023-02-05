import sys

input = sys.stdin.readline

n, m = map(int, input().rstrip('\n').split())

tester = []

for _ in range(n):
    time = int(input().rstrip('\n'))
    tester.append(time)

start = min(tester)
end = (max(tester) * m)

result = 0
while (start <= end):
    mid = (start + end) // 2
    people = 0

    for time in tester:
        people += (mid // time)

    if people < m:
        start = mid + 1

    else:
        result = mid
        end = mid - 1

print(result)