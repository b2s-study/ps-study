import sys


def is_valid(this, other):
    deffrences = 0
    for i in range(len(this)):
        if this[i] != other[i]:
            deffrences += 1
    return deffrences == 1


def dfs(c_idx, target, steps, words):
    global visited, answer

    if words[c_idx] == target:
        answer = min(steps, answer)
        return

    for i in range(len(words)):
        if not visited[i] and is_valid(words[c_idx], words[i]):
            visited[i] = True
            dfs(i, target, steps+1, words)
            visited[i] = False


# dfs로 한단어씩 탐색
# 조회 조건: 알파벳 하나만 바뀌어야 함, 이전에 조회한 것 제외
# 타겟과 일치하면 최소 단계 수 업데이트
def solution(begin, target, words):
    global visited, answer

    answer = sys.maxsize
    words = [begin] + words
    visited = [False] * (len(words) + 2)

    dfs(0, target, 0, words)
    if answer == sys.maxsize:
        answer = 0

    return answer
