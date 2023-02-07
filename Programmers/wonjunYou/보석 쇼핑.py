from collections import defaultdict

def solution(gems):
    total_gems = len(set(gems))

    start = 0
    end = 0

    min_section = len(gems)
    min_section_pos = [start + 1, min_section]

    gem_counter = defaultdict(int)

    while (end < len(gems)):
        gem_counter[gems[end]] += 1
        end += 1

        if len(gem_counter) == total_gems:
            while (start < end):
                if (gem_counter[gems[start]] > 1):
                    gem_counter[gems[start]] -= 1
                    start += 1

                else:
                    if ((end - start) < min_section):
                        min_section = end - start
                        min_section_pos[0], min_section_pos[1] = start + 1, end
                    break

    return min_section_pos