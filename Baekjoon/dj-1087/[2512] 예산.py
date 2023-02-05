import sys

# ======================= init ======================= #

input = sys.stdin.readline

N = int(input())
budget_list = list(map(int, input().split()))
limit = int(input())

# ======================= solve ======================= #
# 핵심 로직 - 상한액 이분 탐색
# 탐색 범위: 0~국가예산(limit)

min_budget, max_budget = 0, max(budget_list)
while (True):
    mid_budget = (min_budget + max_budget) // 2
    if min_budget > max_budget:
        break

    total_budget = 0
    for budget in budget_list:
        if budget < mid_budget:
            total_budget += budget
        else:
            total_budget += mid_budget

    if total_budget <= limit:
        min_budget = mid_budget + 1
    elif total_budget > limit:
        max_budget = mid_budget - 1
    else:
        break

print(mid_budget)
