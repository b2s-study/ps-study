''' 1. 정렬 + greedy 풀이
import sys

input = sys.stdin.readline

n = int(input().rstrip())
budgets = list(map(int, input().rstrip('\n').split()))
total_budget = int(input().rstrip('\n'))

budgets.sort()

budgets_count = len(budgets)

for budget in budgets:
    avg = total_budget / budgets_count

    if (avg > budget):
        total_budget -= budget
        budgets_count -= 1

    else:
        print(int(avg))
        break
else:
    print(budgets[-1])
'''

# 2. 이분 탐색 풀이
import sys

input = sys.stdin.readline

n = int(input().rstrip())
budgets = list(map(int, input().rstrip('\n').split()))
total_budget = int(input().rstrip('\n'))

budgets.sort()

start = 1
end = budgets[-1]

while (start <= end):
    mid = (start + end) // 2
    tmp = 0

    for budget in budgets:
        if (budget < mid):
            tmp += budget
        else:
            tmp += mid

    if tmp <= total_budget:
        start = mid + 1

    else:
        end = mid - 1

print(end)

