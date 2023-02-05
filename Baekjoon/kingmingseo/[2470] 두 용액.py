import sys

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
data.sort()

start = 0
end = N - 1
answer = abs(data[start] + data[end])
ans_s = start
ans_e = end

while (start < end):
    temp = data[start] + data[end]

    if abs(temp) < answer:
        ans_e = end
        ans_s = start
        answer = abs(temp)
        if temp == 0:
            break

    if temp < 0:
        start = start + 1
    elif temp > 0:
        end = end - 1

print(data[ans_s], data[ans_e])


