import sys
import heapq
from collections import deque


class Shark:
    def __init__(self) -> None:
        self.size = 2
        self.eats = 0

    def eat(self):
        self.eats += 1
        if self.eats >= self.size:
            self.size += 1
            self.eats = 0


def is_out_of_range(row, col):
    if (0 <= row < N) and (0 <= col < N):
        return False
    return True


def simulate(srow, scol):
    global shark
    fish_list = []
    min_time = sys.maxsize
    q = deque([(srow, scol)])
    while q:
        row, col = q.popleft()
        for i in range(4):
            nrow = row + drow[i]
            ncol = col + dcol[i]
            if is_out_of_range(nrow, ncol):
                continue

            fish_size = sea[nrow][ncol]
            if simulation[row][col] >= min_time:
                return fish_list[0]

            if simulation[nrow][ncol] == 0 and fish_size <= shark.size:
                q.append((nrow, ncol))
                simulation[nrow][ncol] = simulation[row][col] + 1

            if fish_size != 0 and shark.size > fish_size:
                if min_time == sys.maxsize:
                    shark.eat()
                    min_time = simulation[nrow][ncol]
                    # print("min_time >>", min_time)

                heapq.heappush(fish_list, (nrow, ncol))
                # print(fish_list)
    if len(fish_list) != 0:
        return fish_list[0]
    return (-1, -1)


def update(row, col):
    global simulation, time, shark
    print("========eat=========")
    print("row, col, time, shark.size", row, col, time, shark.size)
    simulation = [[0]*N for _ in range(N)]
    sea[row][col] = 0
    for li in sea:
        print(li)


input = sys.stdin.readline

N = int(input())
sea = []

# bfs로 먹을 수 있는 물고기까지의 최단거리 구하기
# - 여러개일 경우 위쪽, 왼쪽으로 우선순위가 있음
# 물고기 수를 카운팅하여 아기상어 크기 업데이트
# 더이상 먹을 수 없으면 시간 리턴

(srow, scol) = (-1, -1)
for r in range(N):
    row = list(map(int, input().split()))
    if 9 in row:
        (srow, scol) = (r, row.index(9))
    sea.append(row)

simulation = [[0]*N for _ in range(N)]
drow = [-1, 0, 0, 1]
dcol = [0, -1, 1, 0]

time = 0
shark = Shark()
while (srow != -1 and scol != -1):
    time += simulation[srow][scol]
    update(srow, scol)

    srow, scol = simulate(srow, scol)
    # print("srow, scol", srow, scol)
print(time)

# for li in sea:
#     print(li)
