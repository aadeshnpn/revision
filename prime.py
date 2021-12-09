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


##Flags
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def create_peaks(A):
    allpeaks = [False] * len(A)
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            allpeaks[i] = True
    return allpeaks

def check(x, P):
    flag = x
    pos = 0
    while pos < len(P) and flag > 0:
        if P[pos]:
            flag -= 1
            pos += x
        else:
            pos += 1
    return flag ==0

def solution(A):
    # write your code in Python 3.6
    peaks = create_peaks(A)
    peaksum = sum(peaks)
    if peaksum <= 1:
        return peaksum
    else:
        x = peaksum //2
        # print(x)
        if check(x, peaks):
            x += 1
            while check(x, peaks):
                x += 1
            return x-1
        else:
            x -= 1
            while not check(x, peaks):
                x -= 1
            return x


#Peaks
def get_factors(N):
    factors = []
    i = 1
    while (i * i < N):
        if N % i == 0:
            factors.append(i)
        i += 1
    if i*i == N:
        factors.append(i)
    for f in reversed(factors):
        factors.append(N//f)
    return factors

def create_peaks(A):
    allpeaks = [False] * len(A)
    for i in range(1, len(A)-1):
        if A[i-1] < A[i] > A[i+1]:
            allpeaks[i] = True
    return allpeaks

def solution(A):
    # write your code in Python 3.6
    peaks = create_peaks(A)
    # print(peaks)
    factors = get_factors(len(A))
    # print(factors)
    sumpeaks = sum(peaks)
    if sumpeaks <= 1:
        return sumpeaks
    else:
        for i in range(len(factors)-1, -1, -1):
            if factors[i] > sumpeaks:
                pass
            else:
                idx = len(A) // factors[i]
                # print(i)
                k=0
                m= 1
                while k < len(A):
                    # print(k)
                    if peaks[k]:
                        # print(k, m)
                        if k < (idx*m)-1:
                            k = (idx * m)-1
                        else:
                            k += 1
                        m += 1
                    else:
                        k += 1
                # print(m, factors[i])
                if m-1 == factors[i]:
                    return m-1