import sys
input = sys.stdin.readline

n , sum = map(int,input().split())
data = list(map(int,input().split()))
count=0
interval_sum =0
end = 0

for start in range(n):
    while interval_sum < sum and end  <n :
        interval_sum = interval_sum +data[end]
        end = end + 1


    if interval_sum == sum:
        count = count +1

    interval_sum = interval_sum - data[start]

print(count)

