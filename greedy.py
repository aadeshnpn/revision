###AbsDistinct

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    numdict = dict()
    cnt = 0
    for i in range(len(A)):
        val = numdict.get(abs(A[i]), -1)
        if val == -1:
            cnt += 1
            numdict[abs(A[i])] = 1
    return cnt


#### CountDistinctSlices
def solution(M, A):
    # write your code in Python 3.6
    start = 0
    cnt = 0
    if len(A) ==1:
        return 1
    else:
        for start in range(len(A)):
            distdict = dict()
            end = start
            while end < len(A):
                val = distdict.get(A[end], -1)
                if val == -1:
                    # print(start,end)
                    distdict[A[end]] = 1
                    end += 1
                    cnt += 1
                else:
                    break
    return cnt


def solution(M, A):
    # write your code in Python 3.6
    start = 0
    cnt = 0
    if len(A) ==1:
        return 1
    else:
        for start in range(len(A)):
            end = start
            bdist = [False] * (M+1)
            while end < len(A):
                if bdist[A[end]] is False:
                    # print(start,end)
                    bdist[A[end]] = True
                    end += 1
                    cnt += 1
                else:
                    break
    return cnt