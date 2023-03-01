from collections import defaultdict


def dfs(node, info):
    SHIP, WOLF = 0, 1

    animal = info[node]
    state[animal] += 1
    print(state)

    if state[WOLF] >= state[SHIP]:
        state[animal] -= 1
        return

    while graph[node]:
        child = graph[node][0]
        dfs(child, info)
        graph[node].remove(child)
        graph[node].extend(graph[child])


def solution(info, edges):
    global graph, state
    graph = defaultdict(list)
    state = [0, 0]
    for e in edges:
        parent, child = e
        graph[parent].append(child)
    dfs(0, info)

    return state[0]
