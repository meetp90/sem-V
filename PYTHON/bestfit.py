# best fit algorithm
def bestfit(block , process):
    result = [-1]*len(block)
    memWaste = 0
    for i in range(len(process)):
        allocation = [(x - process[i]) for x in block]
        small = min([i for i in allocation if i > 0])
        memWaste += small
        smallLocation = allocation.index(small)
        result[smallLocation] = process[i]
    print("Best Fit = ",result)
    print("Memory wastage = ",memWaste)



# first fit algorithm

def firstfit(block, process):
    result = [-1]*len(block)
    memWaste = 0
    for i in range(len(process)):
        for j in range(len(block)):
            if block[j] >= process[i]:
                result[j] = process[i]
                memWaste += (block[j] - process[i])
    print("First Fit = ",result)
    print("Memory wastage = ",memWaste)

blockSize = input("Enter the memory size : ").split(" ")
processSize = input("Enter the process size : ").split(" ")
blockSize = [int(blockSize[i]) for i in range(len(blockSize)) ]
processSize = [int(processSize[i]) for i in range(len(processSize)) ]
bestfit(blockSize , processSize)