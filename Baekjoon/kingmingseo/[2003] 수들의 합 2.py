import sys
input= sys.stdin.readline

N , M = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = 1
answer = 0
sum = data[0]

while (end < N+1):

    if sum < M and end ==N:
        end = end +1
    elif sum < M :
        sum = sum + data[end]
        end = end+1
    elif sum > M :
        sum = sum -data[start]
        start= start +1


    else :
        answer = answer + 1
        sum = sum -data[start]
        start = start +1

print(answer)