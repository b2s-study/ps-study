import sys

input = sys.stdin.readline

n, c = map(int, input().rstrip('\n').split())

positions = []

for _ in range(n):
    home_position = int(input().rstrip('\n'))

    positions.append(home_position)

positions.sort()

start = 1
end = positions[-1] - positions[0]

while (start <= end):
    mid = (start + end) // 2
    least_pos = positions[0] + mid
    count = 1

    for idx in range(1, len(positions)):
        if positions[idx] >= least_pos:
            count += 1
            least_pos = positions[idx] + mid

    if count >= c:
        start = mid + 1

    else:
        end = mid - 1

print(end)

