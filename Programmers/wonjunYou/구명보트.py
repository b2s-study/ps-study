def solution(people, limit):
    start = 0
    end = len(people) - 1

    pair_count = 0

    people.sort()

    while (start < end):
        if (people[start] + people[end]) <= limit:
            start += 1
            pair_count += 1

        end -= 1

    return len(people) - pair_count