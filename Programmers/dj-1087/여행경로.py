from collections import defaultdict


def dfs(f):
    if len(answer) == length:
        return True

    for i in range(len(direction[f])):
        visited = direction[f][i][1]
        if visited:
            continue

        direction[f][i][1] = True
        t = direction[f][i][0]
        answer.append(t)
        complete = dfs(t)
        if complete:
            return complete

        direction[f][i][1] = False
        answer.pop()

    return False


def solution(tickets):
    global direction, length, answer
    answer = []
    tickets.sort()
    length = len(tickets) + 1

    direction = defaultdict(list)
    # from, to
    for f, t in tickets:
        # 도착지와 visited(T/F)를 추가
        direction[f].append([t, False])

    answer.append("ICN")
    dfs("ICN")

    return answer
