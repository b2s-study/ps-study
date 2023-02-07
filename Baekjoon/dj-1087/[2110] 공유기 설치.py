import sys

input = sys.stdin.readline

N, C = map(int, input().split())
point_list = [int(input()) for _ in range(N)]
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
