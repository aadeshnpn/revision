# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

##MaxProfit

def solution(A):
    # write your code in Python 3.6
    arr = A
    if len(A) <=1:
        return 0
    else:
        max_diff = arr[1] - arr[0]
        min_element = arr[0]

        for i in range( 1, len(A)):
            if (arr[i] - min_element > max_diff):
                max_diff = arr[i] - min_element

            if (arr[i] < min_element):
                min_element = arr[i]

    if max_diff < 0:
        return 0
    else:
        return max_diff