import sys
input = sys.stdin.readline

n, m = map(int,input().split())
data = list(map(int,input().split()))

answer = 0
start =0
end = 1

while(start <= end and end <= n):

    total = sum(data[start:end])

    if (total < m) :
        end = end +1

    elif (total > m ):
        start = start +1

    else :
        answer = answer +1
        end = end+1


print(answer)