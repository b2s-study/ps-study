from collections import defaultdict


def solution(id_list, report, k):
    answer = [0] * len(id_list)

    report = set(report)
    summary_users = defaultdict(set)
    summary_counts = defaultdict(int)
    for log in report:
        user1, user2 = log.split()
        summary_users[user1].add(user2)
        summary_counts[user2] += 1

    for i in range(len(id_list)):
        user = id_list[i]
        for other in summary_users[user]:
            if summary_counts[other] >= k:
                answer[i] += 1
    return answer
