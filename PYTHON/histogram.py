# python experiment 1

# def histogram(l):
#     freq = {}

#     for i in l:
#         if not freq.get(i):
#             freq[i] = 1
#         else:
#             freq[i] += 1

#     res = freq.items()
#     return res


# a = input("Enter the numbers").split(" ")
# a = [int(x) for x in a]
# val = histogram(a)
# answer = sorted(val,key = lambda a:(a[1],a[0]))
# result = list(reversed(answer))

# print(result)


#using sets

def hist(a):
    s = set(a)
    res = []
    
    for i in s:
        res.append((i,a.count(i)))
    return res
    
a = input("Enter the numbers").split(" ")
a = [int(x) for x in a]
val = hist(a)
answer = sorted(val,key = lambda a:(a[1],a[0]))
result = list(reversed(answer))
print(result)
    