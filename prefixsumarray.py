def maxSubArray(a):
    curr_max = a[0]
    max_so_far = a[0]
    for i in range(1, len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far



def minSubArray(a):
    curr_min = a[0]
    min_so_far = a[0]
    for i in range(1, len(a)):
        # print(i, a[i], curr_min, min_so_far)
        curr_min = min(a[i], curr_min + a[i])
        min_so_far = min(min_so_far, curr_min)
    return min_so_far


def maxSubArrayPrefixSum(a):
    import math
    prefixsum = [0] * len(a)
    prefixsum[0] = a[0]
    for i in range(1, len(a)):
        prefixsum[i] = prefixsum[i-1] + a[i]

    min_so_far = 0
    curr_max = -math.inf
    for i in range(len(a)):
        curr_max = max(curr_max, prefixsum[i]- min_so_far)
        min_so_far = min(min_so_far, prefixsum[i])
    return curr_max


def main():
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    b = [2,4,-1,5,6,-2,8]
    print(maxSubArray(b))
    print(minSubArray(a))
    print(maxSubArrayPrefixSum(a))

if __name__ == '__main__':
    main()
