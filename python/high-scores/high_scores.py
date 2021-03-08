def latest(scores:list) -> int:
    return scores.pop()


def personal_best(scores:list) -> int:
    return max(scores)


def personal_top_three(scores:list) -> list:
    return sorted(scores, reverse=True)[:3]
