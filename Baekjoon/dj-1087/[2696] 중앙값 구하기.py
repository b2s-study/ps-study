import sys
import heapq


def insert_heap_node(heap, value, is_max_heap=False):
    node = (-1 * value, value) if is_max_heap else (value, value)
    heapq.heappush(heap, node)


def pop_middle_value(left_max_heap, right_min_heap):
    node = heapq.heappop(right_min_heap) if len(left_max_heap) < len(
        right_min_heap) else heapq.heappop(left_max_heap)
    return node[1]


def print_result(middle_value_list, M):
    index = 0
    while (True):
        if index >= (M//2 + 1):
            break

        buffer = middle_value_list[index: index +
                                   10] if index + 10 <= M else middle_value_list[index:]
        print(*buffer)

        index += 10


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M = int(input())
    print(M//2 + 1)

    number_list = []
    while (True):
        if M < 0:
            break

        buffer = list(map(int, input().split()))
        number_list.extend(buffer)
        M -= 10

    M = len(number_list)
    left_max_heap = []
    right_min_heap = []
    middle_value = 0
    middle_value_list = []
    for i in range(M):
        if i == 0:
            middle_value = number_list[0]
            middle_value_list.append(middle_value)
            continue

        current_value = number_list[i]
        if current_value > middle_value:
            insert_heap_node(right_min_heap, current_value, is_max_heap=False)
            insert_heap_node(left_max_heap, middle_value, is_max_heap=True)

            middle_value = pop_middle_value(left_max_heap, right_min_heap)

        else:
            insert_heap_node(left_max_heap, current_value, is_max_heap=True)
            insert_heap_node(right_min_heap, middle_value, is_max_heap=False)

            middle_value = pop_middle_value(left_max_heap, right_min_heap)

        if i % 2 == 0:
            middle_value_list.append(middle_value)

    print_result(middle_value_list, M)
