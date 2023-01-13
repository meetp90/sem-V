def twoCompliment(num) : 
    oneCompliment = ""
    for i in num:
        if i == "0":
            oneCompliment += "1"
        else:
            oneCompliment += "0"
    return bin(int(oneCompliment,2) + int("1",2)).replace("0b","")

num1 = int(input("enter num1 : "))
num2 = int(input("enter num2 : "))

binNum1 = bin(num1).replace("0b","")

if num2 < 0:
    binNum2 = twoCompliment(bin(num2).replace("0b",""))
else:
    binNum2 = bin(num2).replace("0b","")

maxLen = max(len(binNum1)+1 , len(binNum2) + 1)
print(maxLen)
binNum1 = binNum1.zfill(maxLen)
binNum2 = binNum2.zfill(maxLen)

a = "0" * maxLen
q = binNum2
binNum1Comp = twoCompliment(binNum1)
q1 = "0"

print(binNum1,binNum2,binNum1Comp)
print(q[maxLen - 1])        
for i in range(maxLen):
    if (q[maxLen - 1] == "0" and q1 == "1"):
        a = bin(int(a,2) + int(binNum1,2)).replace("0b","")
        if len(a) > maxLen:
            a = a[1:]
        print("A + M = ",a)
    elif (q[maxLen - 1] == "1" and q1 == "0"):
        a = bin(int(a,2) + int(binNum1Comp,2)).replace("0b","")
        if len(a) > maxLen:
            a = a[1:]
        print("A - M = ",a)
    merge = a + q + q1
    rightShift = merge[0]
    for i in range(len(merge)):
        rightShift += merge[i]
    a = rightShift[:maxLen]
    q = rightShift[maxLen:maxLen*2]
    print("Q",q)
    q1 = rightShift[-1]
print(a,q)

        