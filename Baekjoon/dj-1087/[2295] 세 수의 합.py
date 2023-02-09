import sys

# ======================= init ======================= #

input = sys.stdin.readline

# ======================= solve ======================= #
# 핵심 로직 - 미리 계산한 두 수의 합을 이용하여 세 수의 합을 구한다.
# 시간복잡도 - O(N^2)


N = int(input())
U = [int(input()) for _ in range(N)]

two_sum_set = set()
for i in range(len(U)):
    for j in range(len(U)):
        two_sum = U[i] + U[j]
        two_sum_set.add(two_sum)

max_d = 0
for i in range(len(U)):
    for j in range(i+1, len(U)):
        two_sum = U[j] - U[i]
        if two_sum in two_sum_set:
            d = two_sum + U[i]
            max_d = max(max_d, d)

print(max_d)
