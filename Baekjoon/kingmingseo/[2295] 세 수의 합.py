import sys
input = sys.stdin.readline

n = int(input())
data =[]

for _ in range(n):
    data.append(int(input()))

data.sort()
data_set = set(data)

start = 0
mid = 0
end = 0
answer = 0
max_value = max(data)


while(end < len(data)-1):
    total = data[start] + data[mid] + data[end]

    if start == mid and mid == end and start == mid and total > max_value:
        break

    elif total in data_set and total >= answer :
        print(start, mid, end)
        answer = total
        start = start + 1


    elif total not in data_set and total < max_value:
        start = start + 1

    elif total not in data_set and total > max_value and end < mid:
        end = mid
        start = mid

    elif total not in data_set and total > max_value:
        mid = mid +1
        start = mid

    else :
        start = start +1

print(answer)



