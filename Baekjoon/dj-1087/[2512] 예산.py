import sys

input = sys.stdin.readline

N = int(input())
budget_list = list(map(int, input().split()))
limit = int(input())

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
