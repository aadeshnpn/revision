# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

##MaxProfit

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) <=1:
        return 0
    else:
        max_val = A[1] - A[0]
        min_val = A[0]

        for i in range(1, len(A)):
            if (A[i] - min_val > max_val):
                max_val = A[i] - min_val
            if A[i] < min_val:
                min_val = A[i]

        if max_val <= 0:
            return 0
        else:
            return max_val


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
## MaxSliceSum

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    if len(A) == 1:
        return A[0]
    elif len(A) == 2:
        return max(A[0], A[1], A[0]+A[1])
    elif len(A) ==3:
        return max(A[0], A[1], A[2], A[0]+A[1], A[1]+A[2], A[0]+A[1]+A[2])
    else:
        maxend, maxsum=A[0], A[0]
        for i in range(1, len(A)):
            maxend = max(A[i], maxend+A[i])
            maxsum = max(maxsum, maxend)
        return maxsum

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
## MaxDoubleSliceSum
def solution(A):
    # write your code in Python 3.6
    startarr = [0] * len(A)
    endarr = [0] * len(A)
    for i in range(1, len(A)):
        # print(endarr)
        endarr[i] = max(0, endarr[i-1] + A[i])

    for i in reversed(range(len(A)-1)):
        # print(startarr)
        startarr[i] = max(0, startarr[i+1] + A[i])

    maxsum = 0
    for i in range(1, len(A)-1):
        maxsum = max(maxsum, endarr[i-1] + startarr[i+1])

    return maxsum
