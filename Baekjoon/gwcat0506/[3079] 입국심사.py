# 아 모르겠다...
# 모름..

import sys
input = sys.stdin.readline
N,M = map(int,input().split())

times = [int(input()) for _ in range(N)]

start = min(times)
end = max(times)*M
ans = end

while start<=end:
    total = 0
    mid = (start + end) // 2

    for i in range(N):
        total += mid // times[i]

    if total >= M:
        end = mid -1
        ans = min(mid, ans)

    else:
        start = mid + 1

print(ans)