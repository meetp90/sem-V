# using set

def hist(l):
    s= set(l)
    res = []

    for i in s:
        res.append((i,l.count(i)))

    res.sort(key = lambda x : x[1])
    return res

print(hist([1,1,1,2,2]))
