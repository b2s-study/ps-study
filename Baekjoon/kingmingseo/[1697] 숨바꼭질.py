import sys
from collections import deque
input = sys.stdin.readline

def BFS(x):
    q = deque()
    q.append(x)
    visited[x] = 1

    while q:
        v = q.popleft()

        for flag in range(3):
            if flag == 0:
                nv = v + 1
            elif flag == 1:
                nv = v - 1
            else:
                nv = 2 * v

            if 0 <= nv < len(graph):
                if visited[nv] == 0 :
                    q.append(nv)
                    visited[nv] = visited[v] + 1




Subin, Sister = map(int,input().split())
graph = []
visited = []
for i in range (100001):
    graph.append(i)
    visited.append(0)

BFS(Subin)
print(visited[Sister]-1)