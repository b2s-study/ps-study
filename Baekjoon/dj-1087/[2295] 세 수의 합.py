# - 이슈 사항: 정답 처리가 말이 안 돼... 억울함...
# 아래 반례
# 5
# 3
# 6
# 15
# 1
# 2
# 답: 6
# 출력: 15


import sys

input = sys.stdin.readline

N = int(input())
U = [int(input()) for _ in range(N)]

two_sum_set = set()
for i in range(len(U)):
    for j in range(len(U)):
        # 이거 빼니깐 통과된다고??
        # if i == j:
        #     continue

        two_sum = U[i] + U[j]
        two_sum_set.add(two_sum)

max_d = 0
# U.sort()
for i in range(len(U)):
    for j in range(i+1, len(U)):
        # if i == j:
        #     continue
        two_sum = U[j] - U[i]
        if two_sum in two_sum_set:
            d = two_sum + U[i]
            max_d = max(max_d, d)

print(max_d)
