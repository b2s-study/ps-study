import sys
import heapq


def back():
    global graph, N, X

    time_list = [sys.maxsize] * (N+1)
    pq = []

    time_list[X] = 0
    heapq.heappush(pq, (0, X))

    while pq:
        weight, vertex = heapq.heappop(pq)
        for nw, nv in graph[vertex]:
            nt = nw + weight
            if time_list[nv] <= nt:
                continue

            time_list[nv] = nt
            heapq.heappush(pq, (nt, nv))

    return time_list


def go(start):
    global graph, X

    time_list = [sys.maxsize] * (N+1)
    pq = []

    time_list[start] = 0
    heapq.heappush(pq, (0, start))

    while pq:
        weight, vertex = heapq.heappop(pq)
        if vertex == X:
            return weight

        for nw, nv in graph[vertex]:
            nt = nw + weight
            if time_list[nv] <= nt:
                continue

            time_list[nv] = nt
            heapq.heappush(pq, (nt, nv))

    return sys.maxsize


input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    S, E, T = map(int, input().split())
    graph[S].append((T, E))

back_time = back()
result = 0
for i in range(1, N+1):
    time = go(i)
    result = max(result, time + back_time[i])

print(result)
