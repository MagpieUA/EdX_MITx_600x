def m2(l):
    return sum(l)/len(l)

def v2(l):
    mu = m2(l)
    temp = 0
    for e in l:
        temp += (e-mu)**2
    return temp / len(l)

a = [0,1,2,3,4,5,6,7,8]
b = [5,10,10,10,15]
c = [0,1,2,4,6,8]
d = [6,7,11,12,13,15]
e = [9,0,0,3,3,3,6,6]

print m2(a), m2(b), m2(c), m2(d), m2(e)
print v2(a), v2(b), v2(c), v2(d), v2(e)
