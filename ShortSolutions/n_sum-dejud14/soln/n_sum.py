#Good Luck! You've got this! :)
n,m=map(int,input().split())
listNum = []
while 0<m:
    if 0<m-n:
        m = m - n
        listNum.append(n)
        n = n - 1
    else:
        listNum.append(m)
        m=0
listNum.sort()
print(len(listNum))
listNum[:] = [str(x) for x in listNum]
print(' '.join(listNum))

