# read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())



# solve the problem
A = abs((y1-y2))*abs((x1-x2))


# output the result
print(A)