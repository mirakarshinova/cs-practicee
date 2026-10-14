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
        return 0.0
    return round(sum(scores)/len(scores),2)

def ranking(names, scores) :
    sortnameindrev=sorted(zip(names,scores),key=lambda s:s[1],reverse=True)
    return[names  for names, score in sortnameindrev]


def above_average(names, scores):
    srednee = average(scores)
    res=[]
    for i in range(len(scores)):
        if scores[i]>srednee:
            res.append(names[i])
    return(res)

