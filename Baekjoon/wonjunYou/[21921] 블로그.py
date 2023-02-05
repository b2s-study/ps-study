import sys

input = sys.stdin.readline

n, x = map(int, input().rstrip('\n').split())
visitors = list(map(int, input().rstrip('\n').split()))

start = 0
end = x - 1

max_visitors = sum(visitors[start:end+1])
total_visitors = sum(visitors[start:end+1])

count = 1
while (end < n-1):
    total_visitors -= visitors[start]
    start += 1
    end += 1
    total_visitors += visitors[end]

    if max_visitors < total_visitors:
        max_visitors = total_visitors
        count = 1
        continue

    if max_visitors == total_visitors:
        count += 1

if not max_visitors:
    print("SAD")

else:
    print(max_visitors)
    print(count)