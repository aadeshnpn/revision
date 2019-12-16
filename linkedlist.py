"""Linked list."""

import copy


class node:
    def __init__(self, v):
        self.value = v
        self.next = None


class linkedlist:
    def __init__(self, node):
        self.snode = node

    def add(self, v):
        n  = self.snode
        while True:
            if n.next is None:
                n.next = node(v)
                break
            else:
                n = n.next

    def disLinkedl(self):
        if self.snode is None:
            pass
        else:
            n  = self.snode
            while n is not None:
                print(str(n.value), end=' ')
                n = n.next


def test_simple_linkedlist():
    l1 = linkedlist(node(9))
    l1.add(1)
    l1.add(2)
    l1.add(3)
    l1.add(4)
    l1.add(5)
    l1.disLinkedl()


test_simple_linkedlist()