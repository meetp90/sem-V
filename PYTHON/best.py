def bestFit(process,memory):
    res = [-1] * len(memory)
    for i in range(len(process)):
        hashValue = [x - process[i] for x in memory]
        try:
            minValue = min(x for x in hashValue if x > 0)
        except ValueError:
            break
        location = hashValue.index(minValue)
        res[location] = process[i]
        memory[location] -= process[i]
    print("best Fit = ",res)

def worstFit(process,memory):
    res = [-1] * len(memory)
    for i in range(len(process)):
        hashValue = [x - process[i] for x in memory]
        try:
            maxValue = max(x for x in hashValue if x > 0)
        except ValueError:
            break
        location = hashValue.index(maxValue)
        res[location] = process[i]
        memory[location] -= process[i]
    print("worstFit :",res)

def firstFit(process,memory):
    res = [-1] * len(memory)
    for i in range(len(process)):
        for j in range(len(memory)):
            if process[i] <= memory[j]:
                res[j] = process[i]
                memory[j] -= process[i]
                break
    print("first fit : ",res)

def nextFit(process,memory):
    res = [-1] * len(memory)
    for i in range(len(process)):
        for j in range(len(memory)):
            if process[i] <= memory[j]:
                res[j] = process[i]
                memory[j] -= process[i]
                break
    print("first fit : ",res)


bestFit(memory=[100,500,200,300,600],process=[212, 417, 112, 426])
worstFit(memory=[100,500,200,300,600],process=[212, 417, 112, 426])
firstFit(memory=[100,500,200,300,600],process=[212, 417, 112, 426])