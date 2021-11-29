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


def main():
    pass


if __name__ == '__main__':
    main()
