import sys
import heapq


class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.is_deleted = False

    def delete(self):
        self.is_deleted = True

    def __lt__(self, other):
        return self.value < other.value


class DoublePriorityQueue:
    def __init__(self) -> None:
        self.min_heap = []
        self.max_heap = []

    def insert(self, value):
        self.__clear_deleted_head()
        node = Node(value)
        heapq.heappush(self.min_heap, (value, node))
        heapq.heappush(self.max_heap, (-value, node))

    def pop_max(self):
        if self.__is_empty(self.min_heap):
            return None

        node = heapq.heappop(self.max_heap)[1]
        node.delete()

        self.__clear_deleted_head()
        return node.value

    def pop_min(self):
        if self.__is_empty(self.min_heap):
            return None

        node = heapq.heappop(self.min_heap)[1]
        node.delete()

        self.__clear_deleted_head()
        return node.value

    def __clear_deleted_head(self):
        while (True):
            if self.__is_empty(self.min_heap):
                break

            min_node = self.min_heap[0][1]
            if not min_node.is_deleted:
                break

            heapq.heappop(self.min_heap)

        while (True):
            if self.__is_empty(self.max_heap):
                break

            max_node = self.max_heap[0][1]
            if not max_node.is_deleted:
                break

            heapq.heappop(self.max_heap)

    def __is_empty(self, heap):
        return len(heap) == 0


input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    dpq = DoublePriorityQueue()
    for _ in range(k):
        command_line = input().rstrip().split()
        command = command_line[0]
        parameter = int(command_line[1]) if len(command_line) > 1 else 0

        if command == "I":
            dpq.insert(parameter)
        elif command == "D":
            if parameter == -1:
                dpq.pop_min()
            elif parameter == 1:
                dpq.pop_max()

    if len(dpq.max_heap) == 0:
        print("EMPTY")
    else:
        print(dpq.max_heap[0][1].value, dpq.min_heap[0][1].value)
