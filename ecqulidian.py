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


#CommonPrimeDivisors
## you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def arrayF(n):
    F = [0] * (n+1)
    i =2
    while (i * i <n):
        if (F[i] == 0):
            k = i*i
            while k <=n:
                if F[k] ==0:
                    F[k] = i
                k += i
        i += 1
    return F

def factorization(x,F):
    primefactor = []
    while F[x] > 0:
        primefactor += [F[x]]
        x = x // F[x]
    primefactor += [x]
    return primefactor

def solution(A, B):
    # write your code in Python 3.6
    F = arrayF(max(max(A), max(B)))
    count = 0
    for i in range(len(A)):
        p1 = factorization(A[i], F)
        p2 = factorization(B[i], F)
        if set(p1) == set(p2):
            count += 1
    return count




### CommonPrimeDivisors
#

def gcd(a,b):
    if a % b ==0:
        return b
    else:
        return gcd(b, a % b)

def hassomepm(a, b):
    gcdval = gcd(a,b)
    while a !=1:
        gcda = gcd(a, gcdval)
        if gcda == 1:
            break
        a = a //gcda
    if a != 1:
        return False
    while b !=1:
        gcdb = gcd(b, gcdval)
        if gcdb == 1:
            break
        b = b //gcdb
    return b ==1


def solution(A, B):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A)):
        if hassomepm(A[i], B[i]):
            count +=1
    return count