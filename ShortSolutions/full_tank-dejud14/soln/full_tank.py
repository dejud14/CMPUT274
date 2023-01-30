# Good luck on this morning problem!

leng, cap, st, t = map(int, input().split())
print()
loc = list(input().split())
loc.append(leng)

d = 0
pha = 0
tp = 0
set = 0

if leng == cap:
    tp = leng

else:
    for i in range(len(loc) - 1):
        if (int(loc[i+1]) + set) > cap:
            tp = tp + t
            d = d + int(loc[i])
            pha = pha + 1
            set = -abs(int(loc[i]))

        else:
            pha = pha + 1
    tp = tp + leng
print(tp)
