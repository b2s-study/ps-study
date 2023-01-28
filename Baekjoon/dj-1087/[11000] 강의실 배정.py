import sys
import heapq

input = sys.stdin.readline

N = int(input())

class_list = [tuple(map(int, input().split())) for _ in range(N)]
class_list.sort()

end_time_list = []
for S, T in class_list:

    if len(end_time_list) == 0:
        end_time_list.append(T)
        continue

    latest_end_time = end_time_list[0]
    if latest_end_time <= S:
        heapq.heappop(end_time_list)

    heapq.heappush(end_time_list, T)

room_count = len(end_time_list)
print(room_count)
