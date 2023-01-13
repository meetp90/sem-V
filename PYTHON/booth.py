def twoCompliment(num):
    oneCompliment = ''
    for i in num:
        if i == '0':
            oneCompliment += '1'
        else:
            oneCompliment += '0'
    return bin(int(oneCompliment,2)+int('1',2)).replace("0b","")

n1 = int(input("num1"))
n2 = int(input("num2"))

b1 = bin(n1).replace("0b","")
b2 = bin(n2).replace("0b","")

maxlen = max(len(b1)+1,len(b2)+1)

b1 = b1.zfill(maxlen)
b2 = b2.zfill(maxlen)

bc1 = twoCompliment(b1)
bc1 = bc1.zfill(maxlen)

a = '0'*maxlen
q = b2
m = b1
minusM = bc1
q1 = '0'

for i in range(maxlen):
    if (q[maxlen - 1] == '0' and q1 == '1'):
        a = bin(int(a,2)+int(m,2)).replace("0b","")
        if len(a) > maxlen:
            a = a[1:]
        a = a.zfill(maxlen)
    elif (q[maxlen - 1] == '1' and q1 == '0'):
        a = bin(int(a,2)+int(minusM,2)).replace("0b","")
        if len(a) > maxlen:
            a = a[1:]
        a = a.zfill(maxlen)
    merge = a + q + q1
    rightShift = merge[0]
    for x in range(len(merge) - 1):
        rightShift += merge[x]

    a = rightShift[:maxlen]
    q = rightShift[maxlen:maxlen*2]
    q1 = rightShift[-1]

print(a,q)
    