import sys

input = sys.stdin.readline

remainList = []

for i in range(10):
    
    x = int(input())

    if ((x % 42) not in remainList):
        remainList.append(x % 42)

print(len(remainList))
