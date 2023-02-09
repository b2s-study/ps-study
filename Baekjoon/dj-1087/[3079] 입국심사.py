import sys

input = sys.stdin.readline

N, M = map(int, input().split())
judge_time_list = [int(input()) for _ in range(N)]

min_time, max_time = 0, max(judge_time_list) * M

mid_time = (min_time + max_time) // 2
while(min_time <= max_time):
    mid_time = (min_time + max_time) // 2
    judge_count = 0
    for time in judge_time_list:
        judge_count += mid_time // time

    if judge_count >= M:
        max_time = mid_time - 1
    else:
        min_time = mid_time + 1


print(min_time)
