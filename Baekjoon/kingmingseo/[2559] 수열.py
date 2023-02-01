import sys
input = sys.stdin.readline

N , K = map(int,input().split())
data = list(map(int,input().split()))

temp = sum(data[:K])
answer = temp

for i in range (K , N):
    temp = temp + data[i] - data[i - K]
    if temp > answer:
        answer = temp

print(answer)