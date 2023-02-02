def solution(gems):
    answer = [1, len(gems)]
    current_types = set()
    current_state = {}
    for gem in gems:
        current_state[gem] = 0

    first = 0
    last = 0
    while (True):
        if (first > last) or (last >= len(gems)):
            break

        last_gem = gems[last]
        current_state[last_gem] += 1
        current_types.add(last_gem)
        if gems[first] == gems[last]:
            while (True):
                first_gem = gems[first]
                if current_state.get(first_gem) == 1:
                    break

                first += 1
                current_state[first_gem] -= 1
        # print("[first+1, last+1]:", [first+1, last+1])
        # print("len(current_types), len(current_state):", len(current_types), len(current_state))
        if len(current_types) == len(current_state):
            if last - first < answer[1] - answer[0]:
                answer = [first+1, last+1]
                # 주의
                first += 1
                last = first
                current_types = set()
                for gem in current_state.keys():
                    current_state[gem] = 0
                continue
        last += 1

    return answer
