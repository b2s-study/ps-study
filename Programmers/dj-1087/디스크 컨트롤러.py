import heapq


def solution(jobs):
    answer = 0
    min_heap = []
    for start, required in jobs:
        heapq.heappush(min_heap, (start, required))

    total_time_list = []
    jobs_pq = []
    current_ms = 0
    prev_end = 0
    while (True):
        if (len(min_heap) == 0) and (len(jobs_pq) == 0):
            break

        if len(min_heap) != 0:
            start, required = min_heap[0]
            if current_ms >= start:
                heapq.heappush(jobs_pq, (required, start))
                heapq.heappop(min_heap)
            elif (len(jobs_pq) == 0) and (current_ms < start):
                current_ms = start

        if len(jobs_pq) == 0:
            current_ms += 1
            continue

        if current_ms == prev_end:
            todo_required, todo_start = heapq.heappop(jobs_pq)
            print("current_ms, todo_start, todo_required >>",
                  current_ms, todo_start, todo_required)

            total_time = current_ms - todo_start + todo_required
            total_time_list.append(total_time)
            prev_end += todo_required

        current_ms += 1

    answer = sum(total_time_list) / len(total_time_list)
    print(total_time_list)
    return answer
