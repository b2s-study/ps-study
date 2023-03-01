import sys

sys.setrecursionlimit(10**6)


def matching(first, current, team):
    team.add(current)
    members.remove(current)
    next = selected[current]

    # 팀 O
    if next == first:
        return True
    # 팀 X
    if (next in team) or (next not in members):
        members.add(current)
        return False

    success = matching(first, next, team)
    if not success:
        members.add(current)

    return success


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    selected = [-1] + list(map(int, input().split()))
    members = set(range(1, n+1))
    remains = len(members)
    team_members = set()

    for member in range(1, n+1):
        if member in members:
            matching(member, member, set())

    print(len(members))
