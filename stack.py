# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
## Brackets
def solution(S):
    # write your code in Python 3.6
    stack = []
    for i in range(len(S)):
        if S[i] in [ "(", "{", "["]:
            stack.append(S[i])
        else:
            try:
                if S[i] == ')' and stack[-1] == '(':
                    stack.pop()
                elif S[i] == '}' and stack[-1] == '{':
                    stack.pop()
                elif S[i] == ']' and stack[-1] == '[':
                    stack.pop()
            except IndexError:
                return 0
    if len(stack) ==0:
        return 1
    else:
        return 0


# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
### Fish

def solution(A, B):
    # write your code in Python 3.6
    fishs = []
    count = 0
    for i in range(len(A)):
        if B[i] == 0:
            while fishs:
                P = fishs[-1]
                if P > A[i]:
                    break
                else:
                    fishs.pop()
            else:
                count += 1
        else:
            fishs.append(A[i])
    return count + len(fishs)


#Stonewall
# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    count = 0
    stack = []

    for i in range(len(H)):
        while stack and stack[-1] > H[i]:
            stack.pop()
        if not stack or stack[-1] < H[i]:
            count += 1
            stack.append(H[i])

    return count