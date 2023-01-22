import sys
input=sys.stdin.readline
num1=int(input())
temp1=list(map(int,input().split()))
num2=int(input())
temp2=list(map(int,input().split()))


temp1.sort()


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

for i in range(num2):
    if binary_search(temp1, temp2[i], 0, num1 - 1) is not None:
        print(1, end=' ')
    else:
        print(0, end=' ')