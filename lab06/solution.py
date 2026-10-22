def count_items(values: list)-> dict:
    counts={}
    for i in values:
        counts[i]=counts.get(i,0)+1
    return counts

def unique_sorted(values: list)-> list:
    return sorted(set(values))

#def common(first: list, second: list)-> list:
    #secondset=set(second)
    #return sorted(set[x for x in first if x in secondset])

#def only_in_first(first: list, second: list)->list:
    #return sorted(set(first)-set(second))
