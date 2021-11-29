# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# For example, given the string S = CAGCCTA and arrays P, Q such that:
#     P[0] = 2    Q[0] = 4
#     P[1] = 5    Q[1] = 5
#     P[2] = 0    Q[2] = 6

# the function should return the values [2, 4, 1], as explained above.
## Copyright codility.com


def solution(S, P, Q):
    # write your code in Python 3.6
    A,C,G,T = [-1]*len(S), [-1]*len(S),[-1]*len(S),[-1]*len(S)

    for i in range(len(S)):
        if S[i] == 'A':
            A[i] = i
            C[i] = C[i-1]
            G[i] = G[i-1]
            T[i] = T[i-1]
        elif S[i] == 'C':
            C[i] = i
            A[i] = A[i-1]
            G[i] = G[i-1]
            T[i] = T[i-1]
        elif S[i] == 'G':
            C[i] = C[i-1]
            A[i] = A[i-1]
            T[i] = T[i-1]
            G[i] = i
        else:
            C[i] = C[i-1]
            G[i] = G[i-1]
            A[i] = A[i-1]
            T[i] = i
    results = []
    for k in range(len(Q)):
        if A[Q[k]] >= P[k]:
            results += [1]
        elif C[Q[k]] >= P[k]:
            results += [2]
        elif G[Q[k]] >= P[k]:
            results += [3]
        else:
            results += [4]

    return results
