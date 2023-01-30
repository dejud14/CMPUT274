mix, loc, T = map(int, input().split())
TempF = [int(ind) for ind in input().split()]
TempF.sort()

rng = T*2
maxtemp = TempF[0] + rng
RList = []
cnt = 0
pha = 0

while True:
    pha = 0
    if (loc > len(RList)) and (maxtemp >= TempF[0]):
        RList.append(TempF[0])
        TempF.pop(0)
    else:
        RList = []
        cnt = cnt + 1
        if TempF != []:
            maxtemp = TempF[0] + rng
    if TempF == []:
        cnt = cnt + 1
        break
print(cnt)