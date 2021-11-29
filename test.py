def solution(N):
    # write your code in Python 3.6
    nlist = [i for i in range(-N, N+1)]
    zerolist = []
    midpoint = (len(nlist) // 2)
    if N == 1:
        zerolist.append(nlist[midpoint])
    else:
        if N % 2 == 0:
            right = 1
            left = 1
        else:
            right = 0
            left = 1
        for i in range(0, N):
            if i % 2 == 0:
                j = midpoint + right
                zerolist.append(nlist[j])
                right += 1
            else:
                k = midpoint - left
                zerolist.append(nlist[k])
                left += 1
    return zerolist

print(solution(6))