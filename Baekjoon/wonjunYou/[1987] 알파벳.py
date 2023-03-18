import sys

input = sys.stdin.readline

def translate_letter_2_index(letter):
    return ord(letter) - ord("A")

def dfs(depth, x, y):
    global result

    if depth > result:
        result = depth

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<=nx<r and 0<=ny<c and not visited[nx][ny]):
            letter_index = translate_letter_2_index(board[nx][ny])

            if not check[letter_index]:
                visited[nx][ny] = 1
                check[letter_index] = 1
                dfs(depth + 1, nx, ny)
                visited[nx][ny] = 0
                check[letter_index] = 0

r, c = map(int, input().rstrip('\n').split())
board = [list(input().rstrip('\n')) for _ in range(r)]

check = [0] * 26
visited = [[0] * c for _ in range(r)]
result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

visited[0][0] = 1
check[translate_letter_2_index(board[0][0])] = 1

dfs(1, 0, 0)

print(result)