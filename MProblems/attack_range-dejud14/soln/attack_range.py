# your solution goes here
n,m = input().split()
if 1<=int(m)<=1000 and 1<=int(n)<=1000:
    erange = input()
    erangelist = list(erange.split())
    erangelist = [int(x) for x in erangelist]
    erangelist.sort()
    crange = input()
    crangelist = list(crange.split())
    crangelist = [int(x) for x in crangelist]
    crangelist.sort()
    if max(crangelist)<=min(erangelist):
            print('-1')
    else:
        for i in crangelist:
            if i > max(erangelist):
                print(i)
                break

else:
    exit
