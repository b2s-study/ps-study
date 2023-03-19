import sys

input = sys.stdin.readline

def dfs(x, y, d):
    global count

    if graph[x][y] == 0:
        graph[x][y] = 2   #방문처리
        count += 1         #청소 카운트

    for _ in range(4):
        nd = (d+3) % 4  #왼쪽방향으로 한 칸 돌리기
        nx = x + dx[nd]
        ny = y + dy[nd]
        
        # 이동 위치가 빈 곳이면 탐색
        if graph[nx][ny] == 0:
            dfs(nx, ny, nd)
            return
        
        # 방향 변경
        d = nd

    # 4방향 모두 탐색
    nd = (d + 2) % 4  # 후진방향
    nx = x + dx[nd]
    ny = y + dy[nd]

    # 이동 위치가 벽이라면 리턴
    if graph[nx][ny] == 1:
        return
    
    # 이동 위치가 벽이 아니라면 탐색
    dfs(nx, ny, d)

n, m = map(int, input().rstrip('\n').split())  # n x m 의 방 크기 입력
r, c, d = map(int, input().rstrip('\n').split()) # 로봇 청소기 좌표(r,c) 와 바라보는 방향 d 입력
graph = [list(map(int, input().rstrip('\n').split())) for _ in range(n)]

#북, 동, 하, 서 방향으로 돌기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0
dfs(r, c, d)
print(count)


# while True:
#     flag = 0 #청소 전

#     for _ in range(4):
#         d = (d+3) % 4  #왼쪽방향으로 한 칸 돌리기
#         nr = r + dr[d]
#         nc = c + dc[c]

#         if (0<=nr<n) and (0<=nc<m) and arr[nr][nc] == 0: 
#             if visited[nr][nc] == 0:
#                 visited[nr][nc] == 1
#                 count +=1
#                 r = nr
#                 c = nc
#                 flag = 1 #청소 완료
#                 break

#     if flag == 0:   # 네 방향 모두 청소 할 수 없을 경우
#         if arr[r-dr[d]][c-dc[d]] == 1: # 후진했을 때 벽일 경우 break
#             print(count)
#             break
#         else: #후진했을 때 벽이 아닐 경우 위치 다시 갱신
#             r, c = r-dr[d], c-dc[d]


