import sys
input= sys.stdin.readline

loop = int(input())
two_sum = set()
answer = 0
data = [int(input()) for _ in range(loop)]
data.sort()

for i in range(loop):
    for j in range(loop):
        two_sum.add(data[i]+data[j])



for i in range(loop-1, -1, -1):
    for j in range(i+1):
        if data[i]-data[j] in two_sum and answer < data[i]-data[j]  :
            answer = data[i]


print(answer)



