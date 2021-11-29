# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    minavgsum = (A[0] + A[1]) / 2
    minindx = 0

    if len(A) == 2:
        return minindx
    else:
        for i in range(0, len(A)):
            if i <= len(A)-2:
                slice2avg = (A[i] + A[i+1]) / 2
                if slice2avg < minavgsum:
                    minavgsum = slice2avg
                    minindx = i
            if i <= len(A)-3:
                slice3avg = (A[i] + A[i+1] + A[i+2]) / 3
                if slice3avg < minavgsum:
                    minavgsum = slice3avg
                    minindx = i
    return minindx
