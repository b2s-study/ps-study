import sys
input = sys.stdin.readline

N , X = map(int,input().split())
data = list(map(int,input().split()))

temp = sum(data[:X])
answer = temp
count = 0
temp_list = [answer]

for i in range (X , N):
    temp = temp + data[i] - data[i-X]
    if (temp >= answer):
        answer = temp
        temp_list.append(temp)

if(answer == 0):
    print("SAD")
else:
    print(answer)
    print(temp_list.count(answer))
