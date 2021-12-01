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


### Equi leader O(N^2) solution
def leader(A):
    countdict = dict()
    maxkey,maxval = 0, 0
    for i in range(len(A)):
        val = countdict.get(A[i], 0)
        countdict[A[i]] = val + 1
        if countdict[A[i]] > maxval:
            maxval = countdict[A[i]]
            maxkey = A[i]
    if maxval > len(A) / 2 :
        return maxkey
    else:
        return -1


def solution(A):
    # write your code in Python 3.6
    count = 0
    for i in range(len(A)):
        slice1 = A[:i]
        slice2 = A[i:]
        leader1 = leader(slice1)
        leader2 = leader(slice2)
        if leader1 == leader2 and leader1!=-1:
            count += 1

    return count


2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# from collections import defaultdict
## EquiLeader O(N)

def solution(A):
    # write your code in Python 3.6
    marker_l = dict() # defaultdict(lambda : 0)
    marker_r = dict() # defaultdict(lambda : 0)

    for i in range(len(A)):
        val = marker_r.get(A[i], 0)
        marker_r[A[i]] = val+1

    n_equi_leader = 0
    leader = A[0]
    # print(marker_r)
    for i in range(len(A)):
        valr = marker_r.get(A[i], 0)
        vall = marker_l.get(A[i], 0)
        marker_r[A[i]] = valr - 1
        marker_l[A[i]] = vall + 1
        val = marker_l.get(leader, 0)
        marker_l[leader] = val
        val = marker_r.get(leader, 0)
        marker_r[leader] = val

        if i == 0 or marker_l[leader] < marker_l[A[i]]:
            leader = A[i]

        if (i+1) // 2 < marker_l[leader] and (len(A) - (i+1)) // 2 < marker_r[leader]:
            n_equi_leader += 1

    return n_equi_leader