from collections import deque
import sys

input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    visited[1] = 1

    while q:
        v = q.popleft()

        if v == 100:
            print(board[v])
            break

        for step in dice:
            next = v + step

            if next <= 100 and not visited[next]:
                if next in ladder.keys():
                    next = ladder[next]

                if next in snake.keys():
                    next = snake[next]

                if not visited[next]:
                    visited[next] = 1
                    board[next] = board[v] + 1
                    q.append(next)

dice = [1, 2, 3 ,4 ,5, 6]

n, m = map(int, input().rstrip('\n').split())

board = [0] * 101
visited = [0] * 101

ladder = dict()
snake = dict()

for _ in range(n):
    start, end = map(int, input().rstrip('\n').split())
    ladder[start] = end

for _ in range(m):
    start, end = map(int, input().rstrip('\n').split())
    snake[start] = end

bfs()