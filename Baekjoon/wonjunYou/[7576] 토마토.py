from collections import deque
import sys

def bfs(q):
	while q:
		x, y = q.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if 0<=nx<n and 0<=ny<m:
				#토마토가 들어있지 않은 칸
				if box[nx][ny] == -1:
					continue
				if box[nx][ny] == 0:
					box[nx][ny] = box[x][y] + 1
					q.append((nx, ny))

				else:
					if box[nx][ny] > box[x][y] + 1:
						box[nx][ny] = box[x][y] + 1
						q.append((nx, ny))

m, n = map(int, sys.stdin.readline().rstrip('\n').split())

box = []
isRipe = True

for _ in range(n):
	line = list(map(int, sys.stdin.readline().rstrip('\n').split()))
	if 0 in line:
		isRipe = False
	box.append(line)

if isRipe:
	print(0)
	exit()

q = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
	for j in range(m):
		if box[i][j] == 1:
			q.append((i, j))

bfs(q)

is_possible = True
max_value = 0

for i in range(n):
	for j in range(m):
		if box[i][j] == 0:
			is_possible = False
			break

		max_value = max(max_value, box[i][j])

if not is_possible:
	print(-1)
else:
	print(max_value-1)