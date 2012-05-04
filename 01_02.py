__author__ = 'slaer'
L = (4, 23, 23, 12, 16, 56, 18, 13, 23, 24, 17, 34, 12, 34, 5, 6, 23, 23, 81, 14)
count,maxCount,maxNumber,i,k,x,number = 0,0,0,0,0,0,[]

L1 = list(L)
L1.sort()

print L1
for i in L1:
    if i == x:
        number.append(i)
    x = i

for i in L1:
    if i in number:
        count += 1
        if count < maxCount:
            pass
        else:
            maxCount = count
            maxNumber = i
    else:
        count = 0

print {'Number': maxNumber, 'Counts': maxCount}

