import sys
import heapq

# ======================= init ======================= #

input = sys.stdin.readline

N, K = map(int, input().split())
gem_list = [list(map(int, input().split())) for _ in range(N)]
bag_list = [int(input()) for _ in range(K)]

# ======================= solve ======================= #
# 핵심 로직 - 우선순위 큐
# 1. 허용량이 가장 작은 가방부터 차례대로 보석 무게를 비교하여,
# 2. 담을 수 있는 보석후보를 보석 가격을 우선순위로 최대힙에 넣고,
# 3. 각 가방에 담을 수 있는 가장 높은 보석 가격들의 합을 구한다.

max_heap = []
max_price = 0
gem_list.sort()  # O(N*logN)
bag_list.sort()  # O(N*logN)
for bag in bag_list:  # 사실상 O(N)
    while (True):
        if (len(gem_list) == 0) or (gem_list[0][0] > bag):
            if (len(max_heap) != 0):
                max_price += -1 * heapq.heappop(max_heap)
            break
        weight, price = heapq.heappop(gem_list)
        heapq.heappush(max_heap, -1 * price)
print(max_price)
