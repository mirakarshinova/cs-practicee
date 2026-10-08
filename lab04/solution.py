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

def ranking(names: list[str], scores: list[float]) -> list[str]:
    index= sorted(range())


def above_average(names: list[str], scores: list[float]) -> list[str]:
    srednee = average(scores)
    res=[]
    for i in range(len(scores)):
        if scores[i]>srednee:
            res.append(names[i])
    return(res)
