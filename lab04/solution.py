def winner(names: list[str], scores: list[float]) -> str:
    if not scores:
        return ""
    bestindex=0
    for i in range(1, len(scores)):
        if scores[i]> scores[bestindex]:
            bestindex=i
    return names[bestindex]

def average(scores: list[float]) -> float:
    if not scores:
        return ""
    return round(sum(scores)/len(scores),2)

def
