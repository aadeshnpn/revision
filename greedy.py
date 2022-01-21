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


###O(N) solution
def solution(M, A):
    # write your code in Python 3.6
    front,back,result = 0, 0, 0
    visited = [False] * (M+1)

    while back < len(A):
        if front < len(A) and not visited[A[front]]:
            result += front - back +1
            visited[A[front]] = True
            front += 1
        else:
            visited[A[back]] = False
            back += 1

        if result > 1000000000:
            return 1000000000

    return result



####CountTraiangles
#
# # you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sortedA = sorted(A)
    count = 0
    for i in range(len(A)-2):
        k = i+2
        for j in range(i+1, len(A)):
            while k < len(A) and sortedA[i] + sortedA[j] > sortedA[k]:
                k +=1
            if k > j:
                count += k-j-1
    return count


#MinAbsSumOfTwo

def solution(A):
    # write your code in Python 3.6
    minval = 2000000001
    for i in range(len(A)):
        for j in range(len(A)):
            absval = abs(A[i] + A[j])
            if absval < minval:
                minval = absval
    return minval




# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    sortedA = sorted(A)
    result = abs(sortedA[0] + sortedA[len(A)-1])
    end = len(A) -1
    for i in range(len(A)):
        current = end
        current_result = abs(sortedA[i] + sortedA[current])
        while current >=0 and abs(sortedA[i] + sortedA[current]) <= current_result:
            current_result = abs(sortedA[i] + sortedA[current])
            end = current
            current -= 1
        if current_result < result:
            result = current_result
    return result
