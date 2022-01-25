"""Binary tree."""

class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, tnode):
        if tnode.value < self.data:
            self.left = tnode
        elif tnode.value > self.data:
            self.right = tnode
        else:
            raise 'Duplicate value Error'


def inorderT(root):
    # L, R, Ri
    if root.left is not None:
        inorderT(root.left)
    print(root.data, end=' ')
    if root.right is not None:
        inorderT(root.right)


def preorderT(root):
    # R, L, Ri
    print(root.data, end =' ')
    if root.left is not None:
        preorderT(root.left)
    if root.right is not None:
        preorderT(root.right)

def postorderT(root):
    # L, Ri, R
    if root.left is not None:
        preorderT(root.left)
    if root.right is not None:
        preorderT(root.right)
    print(root.data, end =' ')


def bfs(root):
    queue = []
    queue.append(root)
    data = []
    while len(queue) >= 1:
        data.append(queue[0].data)
        nd = queue.pop(0)
        if nd.left is not None:
            queue.append(nd.left)
        if nd.right is not None:
            queue.append(nd.right)

    return data

def dfs(root):
    stack = []
    stack.append(root)
    data = []
    while len(stack) >=1:
        data.append(stack[-1].data)
        nd = stack.pop()
        if nd.right is not None:
            stack.append(nd.right)
        if nd.left is not None:
            stack.append(nd.left)
    return data


def bfsM(root):
    data = []
    queue = []
    column = 5
    queue.append((root,column))
    left = False
    right = False
    while len(queue) > 0:
        nd,colno = queue.pop(0)
        data.append((nd.data, colno))
        if nd.left is not None:
            queue.append((nd.left, colno-1))
        if nd.right is not None:
            queue.append((nd.right, colno+1))
    return data


def printcolwise(root):
    data = bfsM(root)
    coldict = dict()
    for val,col in data:
        try:
            coldict[col] += [val]
        except KeyError:
            coldict[col] = [val]
    maxcol = max(coldict.keys())
    mincol = min(coldict.keys())

    final = []
    for i in range(mincol, maxcol):
        final += coldict[i]
    print(final)


def main():
    root = node(1)
    two = node(2)
    three = node(3)
    four = node(4)
    five = node(5)
    six = node(6)
    seven = node(7)
    eight = node(8)
    nine = node(9)
    ten = node(10)
    eleven = node(11)

    root.left = two
    root.right = three
    two.left = four
    two.right = five
    three.left = six
    three.right = seven
    four.left = eight
    four.right = nine
    seven.left = ten
    seven.right = eleven
    # array = []
    # inorderT(root)
    # print()
    # preorderT(root)
    # print()
    # postorderT(root)
    # print()
    # print(bfs(root))
    # print(dfs(root))
    # print(bfsM(root))
    printcolwise(root)


if __name__ == '__main__':
    main()
