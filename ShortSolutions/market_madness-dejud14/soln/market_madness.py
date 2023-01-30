# Good luck!
ds = int(input())
value = list(input().split())

purchase = value[0]
ptest = value[:]
ptest.reverse()
plus = 0
if (ptest == value):
    print(0)

else:

    for i in range(ds):
        if (int(value[i]) < int(purchase)):
            purchase = int(value[i])
        elif (int(value[i]) - int(purchase) > int(plus)):
            plus = int(value[i]) - int(purchase)
    print(int(plus))