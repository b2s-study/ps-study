import sys
input = sys.stdin.readline

n = int(input())
idx = 0
result = []

data = list(map(int, input().split()))
index = []
for i in range (1,n+1):
    index.append((i))

temp = data.pop(idx)
result.append(index.pop(idx))

while data:
    if temp < 0:
        idx = (idx + temp) % len(data)
    else:
        idx = (idx + (temp - 1)) % len(data)
    temp = data.pop(idx)
    result.append(index.pop(idx))

for r in result:
    print(r, end=' ')

