import sys

input = sys.stdin.readline

n = int(input().rstrip('\n'))

people = []
rank = [1] * n

for _ in range(n):
    weight, height = map(int, input().rstrip('\n').split())
    people.append((weight, height))

for i in range(len(people)):
    for j in range(len(people)):
        if ((people[i][0] < people[j][0]) and (people[i][1] < people[j][1])):
            rank[i] += 1

print(*rank)