# 이슈사항 - 시간 초과

import sys
import heapq

# - 투 포인터 방식


def two_pointer(array, sum_value):
    # array에 x, y, z 중 하나 제외(예> x)
    # array에 sum(x, y, z)에 해당한다고 예상하는 요소(d) 제외
    # sum_value == y + z = d - x

    left, right = 0, 1
    while (True):
        if (left < 0) or (right >= len(array)):
            break

        current_sum_value = sum([array[left], array[right]])
        # print("left, right, sum", left, right, current_sum_value)
        if current_sum_value > sum_value:
            left -= 1
        elif current_sum_value < sum_value:
            if left == right - 1:
                right += 1
            else:
                left += 1
        else:
            return sum_value
    return None


input = sys.stdin.readline

N = int(input())
number_list = [int(input()) for _ in range(N)]
number_list.sort()

max_heap = []
for i in range(len(number_list)):
    if i >= len(number_list) - 3:
        break

    number = number_list[i]
    for j in range(len(number_list) - 1, -1, -1):
        if j <= i + 2:
            break
        array = number_list[:i] + number_list[i+1:j]
        sum_value = number_list[j] - number
        result = two_pointer(array, sum_value)
        # print("array, sum_value, result>>", array, sum_value, result)
        if result:
            d = result + number
            heapq.heappush(max_heap, (-1*d, d))

print(max_heap[0][1])

# ---------------------
# - 브루트포스 방식
# def get_d_list(case=set()):
#     global number_list, U, d_list
#     # print(case)
#     if len(case) == 3:
#         d = sum(case)
#         if d in U:
#             d_list.append(d)
#             # print(d_list)
#         return

#     for number in number_list:
#         if number not in case:
#             sub_case = case.copy()
#             sub_case.add(number)
#             get_d_list(sub_case)


# input = sys.stdin.readline

# N = int(input())
# number_list = []
# U = set()
# for _ in range(N):
#     number = int(input())
#     number_list.append(number)
#     U.add(number)

# number_list.sort()
# d_list = []
# get_d_list()
# max_d = max(d_list)
# print(max_d)
