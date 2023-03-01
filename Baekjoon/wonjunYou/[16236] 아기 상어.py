from collections import deque
import sys
import heapq

input = sys.stdin.readline

'''
풀이 방법 : BFS
시간 복잡도 : O(n^4)
공간 복잡도 : O(n^2)

1. 아기 상어의 초기 위치를 찾는다.
2. 어떤 물고기들을 먹을 수 있는지 check
3. 상어가 해당 물고기를 먹으러 이동
4. 자신의 크기와 같은 수의 물고기를 먹을 때마다 아기 상어의 크기 증가
5. 엄마 상어에게 도움을 요청한 경우(= 더 이상 먹을 물고기가 없는 경우) 결과 출력
'''

# BFS
def bfs(r, c, shark_size):
    visited = [[0] * n for _ in range(n)]
    q = deque()
    q.append((r, c, 0))
    eatable = []  # 먹을 수 있는 물고기 리스트

    if not visited[r][c]:
        visited[r][c] = 1

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:  # 공간의 범위를 초과하지 않고
                if not visited[nx][ny]:  # 방문하지 않은 칸에 대해
                    visited[nx][ny] = 1  # 방문 처리

                    # case 0: 이동한 칸이 빈칸
                    # case 1: 아기 상어와 크기가 같은 물고기
                    if board[nx][ny] == 0 or board[nx][ny] == shark_size:
                        q.append((nx, ny, dist + 1))

                    # case 2: 아기 상어보다 크기가 작은 물고기
                    elif board[nx][ny] != 0 and board[nx][ny] < shark_size:
                        heapq.heappush(eatable, (dist + 1, nx, ny))

    # 여러 물고기들 중 가장 최우선순위 물고기 정보를 반환
    if eatable:  # heapq를 이용하여 O(log(n))에 처리
        return [eatable[0][1], eatable[0][2], eatable[0][0]]


    else:  # 먹을 수 있는 물고기가 없는 경우 : 종료
        return


if __name__ == "__main__":
    n = int(input().rstrip('\n'))
    board = []

    for _ in range(n):
        board.append(list(map(int, input().rstrip('\n').split())))

    shark_size = 2  # 상어의 크기
    exp = 0  # 상어의 경험치 : shark_size와 같아지면 shark_size + 1

    res = 0

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    # 1. 아기 상어의 초기 위치를 찾는다.
    for r in range(n):
        for c in range(n):
            if board[r][c] == 9:
                board[r][c] = 0
                shark_r, shark_c = r, c  # 상어의 현재 위치 정보 저장
                break

    # 2. 어떤 물고기들을 먹을 수 있는지 check
    while True:
        fish_info = bfs(shark_r, shark_c, shark_size)

        if fish_info:
            shark_r, shark_c, time = fish_info  # 3. 상어가 물고기를 먹으러 이동
            board[shark_r][shark_c] = 0
            exp += 1
            res += time

            # 4. 자신의 크기와 같은 수의 물고기를 먹을 때마다 아기 상어의 크기 증가
            if exp == shark_size:
                shark_size += 1
                exp = 0

        # 5. 엄마 상어에게 도움을 요청한 경우 : 종료
        else:
            print(res)
            break