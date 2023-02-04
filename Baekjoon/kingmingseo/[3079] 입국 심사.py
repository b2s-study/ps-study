import sys
input = sys.stdin.readline

N , M = map(int,input().split())
data = [int(input()) for _ in range(N)]

answer = sys.maxsize

start = 0
end = max(data) * M

while(start <= end):
    mid = (start + end) // 2
    total = 0

    for i in data:
        total = total + (mid // i)

    if total < M :
        start = mid + 1

    else :
        end = mid - 1
        answer = min(mid,answer)


print(answer)


