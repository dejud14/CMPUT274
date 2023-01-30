# your solution goes here
a, m, sf = map(int,input().split())
if m != 0:
    dictio ={"a_"+str(x):[int(c) for c in input().split()] for x in range(a)}
    watched = 0
    mo = dictio.values()
    Lscare = [min([movie[x] for movie in mo]) for x in range(m)]
    Lscare.sort()
    phi = 0
    while sf > 0:
        phg = Lscare[phi]
        if sf - phg >= 0:
            sf = sf - Lscare[phi]
            phi = phi + 1
            watched = watched + 1
        else:
            phi = phi + 1
        if phi >= m:
            break
else:
    watched = 0
print(watched)