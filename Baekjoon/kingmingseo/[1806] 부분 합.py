import sys
input = sys.stdin.readline

N , S = map(int,input().split())
data = list(map(int,input().split()))

start = 0
end = 1
length = 2147483647
sum = data[0]

while (end < N+1):

    if sum >= S and end-start < length :
        length = end - start
        sum = sum - data[start]
        start = start + 1

    elif sum >= S :
        sum = sum - data[start]
        start = start + 1

    elif end == N and sum <S:
        end = end+1

    elif sum < S :
        sum = sum + data[end]
        end = end + 1


if (length==2147483647):
    print(0)
else:
    print(length)




