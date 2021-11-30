# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
### Dominator

def solution(A):
    # write your code in Python 3.6
    countdict = dict()
    maxkey,maxval = 0, 0
    for i in range(len(A)):
        val = countdict.get(A[i], 0)
        countdict[A[i]] = val + 1
        if countdict[A[i]] > maxval:
            maxval = countdict[A[i]]
            maxkey = A[i]
    if maxval > len(A) / 2 :
        for i in range(len(A)):
            if A[i] == maxkey:
                return i
    else:
        return -1