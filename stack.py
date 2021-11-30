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