import sys
import heapq


def solve(n, graph, gates, summits):
    time_list = [sys.maxsize] * (n+1)
    pq = []
    for start in gates:
        heapq.heappush(pq, [0, start, 0])

    result = [sys.maxsize, sys.maxsize]
    max_intensity = sys.maxsize
    while pq:
        time, vertex, intensity = heapq.heappop(pq)
        if max_intensity < time:
            break
        if vertex in summits:
            if (intensity < result[1]) or (intensity == result[1] and vertex < result[0]):
                result = [vertex, intensity]
                max_intensity = intensity
            continue
        for nv, ni in graph[vertex]:
            if time_list[nv] <= ni or nv in gates:
                continue
            time_list[nv] = ni
            heapq.heappush(pq, [ni, nv, max(intensity, ni)])
    return result


def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for _ in range(n+1)]
    for path in paths:
        a, b, time = path
        graph[a].append([b, time])
        graph[b].append([a, time])

    answer = solve(n, graph, set(gates), set(summits))
    return answer
