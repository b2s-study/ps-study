import sys
import heapq


input = sys.stdin.readline

N = int(input())

problem_list = []
for _ in range(N):
    deadline, cup_count = map(int, input().split())
    problem_list.append((deadline, cup_count))

problem_list.sort()

solved_list = []
for deadline, cup_count in problem_list:
    heapq.heappush(solved_list, cup_count)
    if deadline < len(solved_list):
        heapq.heappop(solved_list)

print(sum(solved_list))
