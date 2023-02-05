import math
import sys

input = sys.stdin.readline

city = int(input())
city_budget = list(map(int, input().split()))
country_budget = int(input())

start = 0
end = max(city_budget)
total_budget = 0
ans = 0
if (sum(city_budget) <= country_budget):
    print(max(city_budget))

else:
    while (start <= end):
        mid = (start + end) // 2
        total_budget = 0

        for i in city_budget:
            total_budget = total_budget + min(mid, i)

        if total_budget > country_budget:
            end = mid - 1

        else:
            start = mid + 1
            ans = max(ans, mid)
    print(ans)