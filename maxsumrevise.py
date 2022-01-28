def targetSum(arr, target):
    prefixdict = set()
    prefixsum = 0
    for j in range(len(arr)):
        prefixsum += arr[j]
        prefixdict.add(prefixsum)
        if prefixsum - target in prefixdict:
            return True
    return False


def maxSumArray(arr):
    max_sumfar = arr[0]
    currsum = arr[0]

    for i in range(1, len(arr)):
        currsum = max(arr[i], currsum + arr[i])
        max_sumfar = max(max_sumfar, currsum)

    return max_sumfar


def main():
    arr = [1,-2,2,5,-2,3,10,7]
    # print(targetSum(arr, 10))
    print(maxSumArray(arr))


if __name__ == '__main__':
    main()