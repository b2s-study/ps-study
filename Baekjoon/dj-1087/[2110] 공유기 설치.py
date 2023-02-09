import sys

# ======================= init ======================= #

input = sys.stdin.readline

N, C = map(int, input().split())
point_list = [int(input()) for _ in range(N)]

# ======================= solve ======================= #
# 핵심 로직 - 두 집 사이의 거리를 이분탐색으로 찾는다.
# 1. 최소 거리는 1, 최대 거리는 가장 먼 두 집 사이의 거리이다.
# 2. 중간 거리를 기준으로 공유기를 설치할 수 있는지 확인한다.
# 3. 공유기를 설치할 수 있다면, 최소 거리를 중간 거리 + 1로 갱신한다.
# 4. 공유기를 설치할 수 없다면, 최대 거리를 중간 거리 - 1로 갱신한다.
# 5. 최소 거리가 최대 거리보다 커지면, 최소 거리를 출력한다.
#
# 시간복잡도 - O(NlogN + NlogM), N: 집의 개수, M: 집의 좌표의 최대값

point_list.sort()

min_distance, max_distance = 0, point_list[-1] - point_list[0]
result = 0
while(min_distance <= max_distance):
    mid_distance = (min_distance + max_distance) // 2

    count = 1
    prev_point = point_list[0]
    for point in point_list:
        if point - prev_point >= mid_distance:
            count += 1
            prev_point = point

    if count >= C:
        min_distance = mid_distance + 1
        result = mid_distance
    else:
        max_distance = mid_distance - 1

print(result)
