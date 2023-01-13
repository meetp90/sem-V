def twoCompliment(num):
    oneCompliment = ""
    for i in num:
        if i == "0":
            oneCompliment += "1"
        else:
            oneCompliment += "0"

    return bin(int(oneCompliment,2) + int("1",2)).replace("0b","")

num1 = int(input("num1 : "))
num2 = int(input("num2 : "))

binNum1 = bin(num1).replace("0b","")
binNum2 = bin(num2).replace("0b","")

maxLen = len(binNum1) + 1 
binNum2 = binNum2.zfill(maxLen)
binNum1 = binNum1.zfill(maxLen - 1)

q = binNum1
M = binNum2
minumM = twoCompliment(binNum2)
count = maxLen - 1
a = "0"*maxLen
leftShift = ''

while count > 0:
    merge = a + q
    leftShift = merge[1:]
    a = leftShift[:maxLen]
    a = bin(int(a,2) + int(minumM,2)).replace("0b","")
    if len(a) > maxLen:
        a = a[1:]
    a = a.zfill(maxLen)
    if a[0] == "0":
        leftShift = a + q[1:]
        leftShift += "1"
    else:
        a = bin(int(a,2) + int(M,2)).replace("0b","")
        if len(a) > maxLen:
            a = a[1:]
        a = a.zfill(maxLen)
        leftShift = a + q[1:]
        leftShift += "0"
    a = leftShift[:maxLen]
    q = leftShift[maxLen:]
    count -= 1

if a[0] == "1":
    a = bin(int(a,2) + int(M,2)).replace("0b","")
    if len(a) > maxLen:
        a = a[1:]

print(a,q)