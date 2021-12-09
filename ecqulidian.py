###ChocolatesByNumbers

def solution(N, M):
    # write your code in Python 3.6
    chocolates = dict()
    chocolates[0] = 1
    X = 0
    count = 0
    while True:
        X = (X + M) % N
        if chocolates.get(X, 0) != 0:
            break
        else:
            chocolates[X] = 1
        count += 1
        if count >= N:
            break
    return len(chocolates.keys())

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def gcd(a,b):
    if a % b ==0:
        return b
    else:
        return gcd(b, a % b)

def solution(N, M):
    # write your code in Python 3.6
    g = gcd(N, M)
    # lcd = (M * N ) // g
    # print(g, lcd)
    return N // g # (M * N)  // (M * g)