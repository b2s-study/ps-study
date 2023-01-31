import sys
input = sys.stdin.readline

data_num = int(input())
data = set(map(int,input().split()))

check_num = int(input())
check = list(map(int,input().split()))

for check_data in check:
    if check_data in data:
        print(1)
    else:
        print(0)



