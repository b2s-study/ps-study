import sys
from collections import deque
input = sys.stdin.readline
def BFS(pos):
    q = deque()
    q.append(pos)

    while q:
        V = q.popleft()

        if graph[V] != 0 :
            temp = V
            V = graph[V]
            visited[V] = visited[temp]

        for i in range(1, 7):
            NV = V + i

            if NV <= 100 and visited[NV] == 0 :
                q.append(NV)
                visited[NV] = visited[V] + 1

graph = [0 for x in range(0,101)]
visited = [0 for x in range(0,101)]
ladder , snake = map(int,input().split())

for _ in range(ladder):
    x , y = map(int,input().split())
    graph[x] = y

for _ in range(snake):
    x, y = map(int, input().split())
    graph[x] = y

BFS(1)

print(visited[100])
