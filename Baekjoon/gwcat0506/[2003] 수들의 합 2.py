import sys
input = sys.stdin.readline

n , m = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = 1
answer = 0

while (end <= n):
    total = sum(data[start:end])        #연속된 수열의 합
    # print('start',start,'end',end,'total',total)
    if(total < m):
        end = end +1

    elif(total > m):
        start = start + 1

    else:
        # print(start,end)
        # print(data[start:end])
        answer = answer + 1
        end = end +1

print(answer)