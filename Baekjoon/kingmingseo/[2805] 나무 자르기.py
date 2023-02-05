import sys
input = sys.stdin.readline

tree , limit = map(int,input().split())
data = list(map(int,input().split()))
data.sort()

start = 0
end = data[-1]

ans = 0
while (start <= end):
    mid = (start + end) // 2
    total = 0

    for i in data:
        if i > mid:
            total = total + (i - mid)

    if total >= limit : #나무를 가져갈 수 있으면 절단기 한계를 더 높여보는 방향으로
        start = mid + 1
        ans = max(ans, mid)

    else: # 나무를 가져갈 수 없으면 절단기 한계를 더 낮춰서 나무를 더 가져가는 방향으로
        end = mid - 1


