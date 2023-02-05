import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

values = list(map(int, input().rstrip('\n').split()))

values.sort()

start = 0
end = n - 1

total = float('inf')
result_x, result_y = 0, 0

while (start < end):
    if abs(values[start] + values[end]) < total:
        total = abs(values[start] + values[end])

        result_x = start
        result_y = end

        if abs(values[start] + values[end]) == 0:
            break

    if (values[start] + values[end]) < 0:
        start += 1

    elif (values[start] + values[end]) > 0:
        end -= 1

print(values[result_x], values[result_y])