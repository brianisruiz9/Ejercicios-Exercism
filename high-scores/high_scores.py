def latest(scores):
    scores.remove(0)
    last = min(scores)
    return last


def personal_best(scores):
    best = max(scores)
    return best

def personal_top_three(scores):
    scores.sort(reverse=True)
    return scores[0:3]
