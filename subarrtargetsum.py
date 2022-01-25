# Sonitnous sequence of intergers sums up to target


def sumtarget(arr, target):
    start,end = 0,0
    # print(arr, target)
    for i in range(len(arr)):
        sumarr = 0
        start = i
        end = start
        while end != len(arr):
            sumarr += arr[end]
            if sumarr == target:
                return True
            elif sumarr < target:
                end += 1
            else:
                break

    return False


def main():
    arr = [1,2,5,2,3,10,7]
    for i in range(1,31):
        print(i, sumtarget(arr, i))


if __name__ == '__main__':
    main()