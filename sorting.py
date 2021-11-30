# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

## Distinct
def solution(A):
    # write your code in Python 3.6
    dis = dict()
    dvalues = 0
    for i in range(len(A)):
        val = dis.get(A[i], 0)
        if val == 0:
            dvalues += 1
            dis[A[i]] = 1
    return dvalues


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

## MaxProductofThree
def solution(A):
    # write your code in Python 3.6
    A.sort()
    return max(A[-1]* A[-2]* A[-3], A[0]*A[-1]*A[1])


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

## Traingle
def solution(A):
    # write your code in Python 3.6
    if len(A) < 3:
        return 0
    else:
        A.sort()
        for i in range(len(A)):
            if len(A)-i >=3:
                # print(i, A[i], A[i+1], A[i+2])
                if A[i] + A[i+1] > A[i+2]:
                    return 1
        return 0


## NumberofDiscIntersections naive solution
def solution(A):
    # write your code in Python 3.6
    minmax = []
    intersect = 0
    sortedA = sorted(enumerate(A), key=lambda x:x[1], reverse=True)
    # print(sortedA)
    for values in sortedA:
        i = values[0]
        val = values[1]
        minr = i - val
        maxr = i + val
        minmax.append((minr, maxr))

    for j in range(len(A)):
        first = minmax[j]
        for k in range(j+1, len(A)):
            comp = minmax[k]
            if first[1] >= comp[0] >= first[0]  or first[1] >= comp[1] >= first[0]:
                # print(j,k, first, comp, True)
                intersect += 1
            # else:
                # print(j,k, first, comp, False)

    return intersect


### O(N) solution
def solution(A):
    # write your code in Python 3.6
    result = 0
    dps = [0] * len(A)
    dpe = [0] * len(A)
    t = len(A)-1
    for i in range(0, len(A)):
        s = (i-A[i]) if i > A[i] else 0
        e = (i+A[i]) if t-i > A[i] else t
        dps[s] += 1
        dpe[e] += 1
    t = 0
    for i in range(len(A)):
        if dps[i] > 0:
            result += t * dps[i]
            result += dps[i] * (dps[i] - 1) //2
            if result > 1e7:
                return -1
            t += dps[i]
        t -= dpe[i]
    return result


#### O(N * log(N)) solution
def soution(A):
    events = []
    for i, a in enumerate(A):
        events += [(i-a, +1), (i+a, -1)]
    events.sort(key=lambda x: (x[0], -x[1]))
    intersections, active_circles = 0, 0
    for _, circle_count_delta in events:
        intersections += active_circles * (circle_count_delta > 0)
        active_circles += circle_count_delta
        if intersections > 1E7:
            return -1
    return intersections