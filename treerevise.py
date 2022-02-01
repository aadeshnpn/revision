from tree import inorderT, preorderT


class node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None


def create_tree(a=[1,2,3,4,5,6,7,8,9,10,11]):
    nodes = [node(i) for i in a]
    j = 1
    for i in [0,1,2,3,6]:
        nodes[i].left = nodes[j]
        j = j+2
    j = 2
    for i in [0,1,2,3,6]:
        nodes[i].right = nodes[j]
        j = j +2
    return nodes[0]


def bfs(root):
    queue = [root]
    values = []
    while len(queue) >= 1:
        popped = queue.pop(0)
        values.append(popped.value)
        if popped.left is not None:
            queue.append(popped.left)
        if popped.right is not None:
            queue.append(popped.right)

    print('BFS', values)


def dfs(root):
    stack = [root]
    values = []

    while len(stack) >= 1:
        popped = stack.pop()
        values.append(popped.value)
        if popped.right is not None:
            stack.append(popped.right)
        if popped.left is not None:
            stack.append(popped.left)

    print('DFS', values)


def preorder(root):
    # root,left,right
    print(root.value, end=" ")
    if root.left is not None:
        preorder(root.left)
    if root.right is not None:
        preorder(root.right)

def inorder(root):
    # left,root,right
    if root.left is not None:
        inorder(root.left)
    print(root.value, end=" ")
    if root.right is not None:
        inorder(root.right)

def postorder(root):
    # left,right,root
    if root.left is not None:
        postorder(root.left)
    if root.right is not None:
        postorder(root.right)
    print(root.value, end=" ")


def main():
    root = create_tree()
    bfs(root)
    dfs(root)
    preorder(root); print()
    inorder(root); print()
    postorder(root); print()


if __name__ == "__main__":
    main()