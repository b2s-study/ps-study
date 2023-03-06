import sys

sys.setrecursionlimit(10**6)


def matching(current, team=[]):
    global selected, visited
    team.append(current)
    visited[current] = True
    next = selected[current]

    if visited[next]:
        if next in team:
            return team[team.index(next):]
        return []

    return matching(next, team)


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    selected = [-1] + list(map(int, input().split()))
    visited = [False] * (n+1)
    remains = n

    for member in range(1, n+1):
        if not visited[member]:
            team = matching(member, [])
            remains -= len(team)

    print(remains)
