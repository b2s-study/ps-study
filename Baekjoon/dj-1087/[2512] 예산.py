# 이슈사항 - 시간 초과

import sys

input = sys.stdin.readline

N = int(input())
budget_list = list(map(int, input().split()))
limit = int(input())

budget_list.sort()
min_budget, max_budget = budget_list[0], budget_list[-1]
while (True):
    if min_budget > max_budget:
        break

    mid_budget = (min_budget + max_budget) / 2
    total_budget = 0
    for budget in budget_list:
        if budget < mid_budget:
            total_budget += budget
        else:
            total_budget += mid_budget

    if total_budget <= limit:
        min_budget += 1
    else:
        max_budget -= 1

# result = int((min_budget + max_budget) / 2)
print(max_budget)


# 블로그 정답 코드
# input = sys.stdin.readline

# N = int(input())
# cities = list(map(int, input().split()))
# budgets = int(input())  # 예산
# start, end = 0, max(cities)  # 시작 점, 끝 점

# # 이분 탐색
# while start <= end:
#     mid = (start+end) // 2
#     total = 0  # 총 지출 양
#     for i in cities:
#         if i > mid:
#             total += mid
#         else:
#             total += i
#     if total <= budgets:  # 지출 양이 예산 보다 작으면
#         start = mid + 1
#     else:  # 지출 양이 예산 보다 크면
#         end = mid - 1
# print(end)
