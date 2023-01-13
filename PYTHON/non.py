def twoCompliment(num):
    oneCompliment = ''
    for i in num:
        if i == "0":
            oneCompliment += '1'
        else:
            oneCompliment += "0"
    return bin(int(oneCompliment,2) + int("1", 2)).replace("0b","")

num1 = int(input("num1 :"))
num2 = int(input("num2 :"))

binNum1 = bin(num1).replace("0b","")
binNum2 = bin(num2).replace("0b","")

maxLen = len(binNum1)

binNum1 = binNum1.zfill(maxLen)
binNum2 = binNum2.zfill(maxLen + 1)

binNum2Comp = twoCompliment(binNum2)
binNum2Comp = binNum2Comp.zfill(maxLen)

count = maxLen
m = binNum2
minusM = binNum2Comp
q = binNum1

a = "0" * (maxLen+1)
leftShift = ""

while count > 0:
    merge = a + q
    leftShift = merge[1:]
    a = leftShift[:maxLen+1]

    if a[0] == "1":
        a = bin(int(a,2) + int(m,2)).replace("0b","")
        if len(a) > maxLen + 1:
            a = a[1:]
        a = a.zfill(maxLen+1)
    else:
        a = bin(int(a,2) + int(minusM,2)).replace("0b","")
        if len(a) > maxLen+1:
            a = a[1:]
        a = a.zfill(maxLen+1)

    leftShift = a + q[1:]
    if a[0] == "1":         
        leftShift += "0"
    else:
        leftShift += "1"
    count -= 1

    a = leftShift[:maxLen+1]
    q = leftShift[maxLen+1:]

if a[0] == "1":
    a = bin(int(a,2) + int(m,2)).replace("0b","")
    if len(a) > maxLen:
        a = a[1:]

print(a,q)