def count_items(values):
    counts={}
    for i in values:
        counts[i]=counts.get(i,0)+1
    return counts

def unique_sorted(values) :
    return sorted(set(values))

def common(first, second):
    secondset=set(second)
    return sorted(set(x for x in first if x in secondset))

def only_in_first(first, second):
    return sorted(set(first)-set(second))
