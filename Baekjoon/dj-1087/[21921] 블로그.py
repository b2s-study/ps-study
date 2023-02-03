import sys

input = sys.stdin.readline

N, X = map(int, input().split())
visitant_list = list(map(int, input().split()))

start = 0
max_sum = sum(visitant_list[start:start+X])
current_sum = sum(visitant_list[start:start+X])
max_period_count = 0
while (True):
    if current_sum > max_sum:
        max_sum = current_sum
        max_period_count = 1

    elif current_sum == max_sum:
        max_period_count += 1

    if start + X >= len(visitant_list):
        break

    # print("start, start+X >>", start, start+X)
    # print("current_sum, max_sum >>", current_sum, max_sum)

    current_sum = current_sum - visitant_list[start] + visitant_list[start+X]
    start += 1
    # print("max_period_count >>", max_period_count)

if max_sum == 0:
    print("SAD")
else:
    print(max_sum)
    print(max_period_count)
