import sys
from collections import defaultdict


def dfs(person, frends):
    if len(frends) == 5:
        return True

    for other in friendship.get(person):
        if other not in frends:
            frends.add(other)
            result = dfs(other, frends)
            frends.remove(other)

            if result == True:
                return result

    return False


input = sys.stdin.readline

N, M = map(int, input().split())
friendship = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    friendship[a].append(b)
    friendship[b].append(a)

find = False
for a in friendship:
    find = dfs(a, set([a]))
    if find:
        print(1)
        exit()

print(0)
