import sys
input = sys.stdin.readline


N , M = map(int,input().split())
data = []
answer = 2147483647

for i in range(N):
    data.append(int(input()))

start = 0
end = 0
data.sort()

while (start < N and end < N):
    value = data[end] - data[start]


    if value >= M and answer > value:
        answer = value
        start= start+1

    elif (value >= M):
        start = start +1

    else:
        end= end+1
print(answer)
