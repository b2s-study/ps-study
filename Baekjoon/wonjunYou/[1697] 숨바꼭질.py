from collections import deque
import sys

def bfs():
	q = deque()
	q.append(n)

	while q:
		point = q.popleft()

		if point == k:
			print(points[k])
			break

		for np in (point-1, point+1, 2*point):
			if 0<=np <= 100000 and not points[np]:
				points[np] = points[point] + 1
				q.append(np)
n, k = map(int , sys.stdin.readline().rstrip('\n').split())

points = [0 for _ in range(100001)]

bfs()