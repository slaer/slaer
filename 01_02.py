__author__ = 'slaer'
L = (4, 23, 23, 12, 16, 56, 18, 13, 23, 24, 17, 34, 12, 34, 5, 6, 23, 23, 81, 14)
L1 = list(L)
L1.sort()
x = 0
k = 0
print L1

for i in L1:
    if i == x:
        print i
        k += 1


    x = i
print k

