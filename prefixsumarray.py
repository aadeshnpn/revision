def maxSubArray(a):
    curr_max = a[0]
    max_so_far = a[0]
    for i in range(len(a)):
        curr_max = max(a[i], curr_max + a[i])
        max_so_far = max(max_so_far, curr_max)
    return max_so_far


def main():
    a = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(maxSubArray(a))


if __name__ == '__main__':
    main()
