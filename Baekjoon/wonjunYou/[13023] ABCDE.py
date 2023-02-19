import sys

input = sys.stdin.readline

def dfs(v, depth):
    if depth == 4:
        print(1)
        exit()

    for friend in friends[v]:
        if not visited[friend]:
            visited[friend] = True
            dfs(friend, depth + 1)
            visited[friend] = False

n, m = map(int, input().rstrip('\n').split())

friends = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    person1, person2 = map(int, input().rstrip('\n').split())
    friends[person1].append(person2)
    friends[person2].append(person1)

for person in range(n):
    visited[person] = True
    dfs(person, 0)
    visited[person] = False

print(0)