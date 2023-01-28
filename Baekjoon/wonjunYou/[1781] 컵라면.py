import sys
import heapq

input = sys.stdin.readline

n = int(input().rstrip('\n'))

problems = []
rewards = []

for _ in range(n):
    deadline, noodles = map(int, input().rstrip('\n').split())
    problems.append((deadline, noodles))

for problem in sorted(problems):
    deadline = problem[0]
    heapq.heappush(rewards, problem[1])

    if len(rewards) > deadline:
        heapq.heappop(rewards)

print(sum(rewards))


