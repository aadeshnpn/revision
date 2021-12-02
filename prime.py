# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

###CountFactors

def solution(N):
    # write your code in Python 3.6
    factors = 0
    i = 1
    while (i * i < N):
        if N % i == 0:
            factors += 2
        i += 1
    if i*i == N:
        factors += 1

    return factors



# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
###MinPerimeterRectangle

def solution(N):
    # write your code in Python 3.6
    factors = []
    i = 1
    while (i * i < N):
        if N % i == 0:
            factors.append(i)
        i += 1
    if i*i == N:
        factors.append(i)

    minper = 2*(N+1)

    for f in range(len(factors)):
        a = factors[f]
        b = N//a
        # print(a,b)
        if 2* (a+b) < minper:
            minper = 2 *(a+b)
    return minper