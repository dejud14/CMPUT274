# your solution goes here
n = input()
if 1<=int(n)<=10000:
    inList = list(input())
    if int(inList.count('#')) == int(inList.count('b')):
        print(0)
    else:
        sharpList = (int(inList.count('#'))-int(inList.count('b')))*['#']
        bList = (int(inList.count('b'))-int(inList.count('#')))*['b']
        fAns= ''.join(sharpList + bList)
        print(fAns)
else:
    exit