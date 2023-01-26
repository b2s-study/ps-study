import sys
import heapq


def insert_heap_node(heap, value, is_max_heap=False):
    node = (-1 * value, value) if is_max_heap else (value, value)

    heapq.heappush(heap, node)
    return


def pop_middle_value(left_max_heap, right_min_heap):
    node = heapq.heappop(right_min_heap) if len(left_max_heap) < len(
        right_min_heap) else heapq.heappop(left_max_heap)
    return node[1]


input = sys.stdin.readline

N = int(input())

middle_value = 0
left_max_heap = []
right_min_heap = []
for i in range(N):
    value = int(input())

    if i == 0:
        middle_value = value

        print(middle_value)
        continue

    if value < middle_value:
        insert_heap_node(left_max_heap, value, is_max_heap=True)
        insert_heap_node(right_min_heap, middle_value, is_max_heap=False)

        middle_value = pop_middle_value(left_max_heap, right_min_heap)

    else:
        insert_heap_node(right_min_heap, value, is_max_heap=False)
        insert_heap_node(left_max_heap, middle_value, is_max_heap=True)

        middle_value = pop_middle_value(left_max_heap, right_min_heap)

    print(middle_value)
