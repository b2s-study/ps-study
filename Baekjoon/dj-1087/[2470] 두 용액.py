import sys

# ======================= init ======================= #

input = sys.stdin.readline

N = int(input())
density_list = list(map(int, input().split()))

# ======================= solve ======================= #
# 핵심 로직 - 투 포인터
# 사전 작업: 용액 농도 리스트를 오름차순으로 정렬
# 1. 가장 왼쪽과 가장 오른쪽 용액 혼합
# 2. 혼합한 용액이 0보다 클 경우 오른쪽 인덱스 -1 이동
#    *통상적인 경우, 왼쪽 +1을 하게 되면 혼합한 농도가 이전에 비해 0보다 더 멀어짐
# 3. 혼합한 용액이 0보다 작을 경우 왼쪽 인덱스 +1 이동
#    *통상적인 경우, 오른쪽 -1을 하게 되면 혼합한 농도가 이전에 비해 0보다 더 멀어짐
# 4. 만약 혼합한 용액 농도의 절댓값이 이전 혼합 용액 농도의 절댓값보다 작다면,
#    이전 혼합 용액 농도의 절댓값을 현재 값으로 갱신
# 2-4를 "왼쪽 인덱스 > 오른쪽 인덱스"가 될 때까지 계속 수행
#
# 시간복잡도 - O(NlogN), sort() - NlogN, 투 포인터 - N


density_list.sort()
absolute_density = abs(density_list[0] + density_list[-1])
left, right = 0, len(density_list) - 1
answer = []
while (left < right):
    current_desity = density_list[left] + density_list[right]
    if abs(current_desity) <= absolute_density:
        answer = [density_list[left], density_list[right]]
        absolute_density = abs(current_desity)

    if current_desity > 0:
        right -= 1
    else:
        left += 1

print(*answer)
