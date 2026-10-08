def winner(names, scores) :
    if not scores:
        return ""
    bestindex=0
    for i in range(1, len(scores)):
        if scores[i]> scores[bestindex]:
            bestindex=i
    return names[bestindex]

def average(scores) :
    if not scores:
        return ""
    return round(sum(scores)/len(scores),2)

def ranking(names, scores) :
    sortedind=sorted(zip(names,scores),key=lambda s:s[1],reverse=True)
    return[name  for name, scores in sortedind]


def above_average(names, scores):
    srednee = average(scores)
    res=[]
    for i in range(len(scores)):
        if scores[i]>srednee:
            res.append(names[i])
    return(res)

