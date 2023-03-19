import sys

input = sys.stdin.readline

def check(sequence):
    for step in range(1, len(sequence) // 2 + 1):
        if sequence[-step:] == sequence[-(2*step): -step]:
            return False
    return True

def dfs(depth, prev, sequence):
    if depth == n:
        print(sequence)
        exit()

    for number in range(1, 4):
        if prev != number:
            if check(sequence + str(number)):
                dfs(depth + 1, number, sequence + str(number))

n = int(input().rstrip('\n'))

dfs(0, 0, '')