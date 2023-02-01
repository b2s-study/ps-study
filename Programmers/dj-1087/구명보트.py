def solution(people, limit):
    pair = 0
    people.sort()

    left, right = 0, len(people)-1

    while (True):
        if left >= right:
            break

        if people[left] + people[right] <= limit:
            pair += 1
            left += 1

        right -= 1

    return len(people) - pair
