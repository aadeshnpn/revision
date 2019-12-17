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
        n = self.snode
        while n.next is not None:
            n = n.next
        n.next = node(v)


    def addIdx(self, idx, v):
        j = 0
        prev = None
        next = None
        n = self.snode
        while n is not None:
            curr = n
            if j == idx:
                temp = node(v)
                prev.next = temp
                temp.next = curr
            prev = curr
            j += 1
            n = n.next


    def remove(self, v):
        prev = None
        next = None
        n = self.snode
        while n is not None:
            curr = n
            next = curr.next
            if curr.value == v:
                prev.next = next
            prev = curr
            n = n.next


    def removeIdx(self, idx):
        prev = None
        next = None
        n = self.snode
        j = 0
        while n is not None:
            curr = n
            next = curr.next
            if j == idx:
                prev.next = next
            prev = curr
            n = n.next
            j += 1


    def displaylList(self):
        n = self.snode
        while n is not None:
            print(n.value, end=' ')
            n = n.next
        print()


    def reverse(self):
        n = self.snode
        prev = None
        while n is not None:
            curr = n
            n = curr.next
            curr.next = prev
            prev = curr
            if n is not None:
                self.snode = n

def test():
    l1 = linkedlist(node(0))
    l1.add(1)
    l1.add(2)
    l1.add(3)
    l1.add(4)
    l1.displaylList()
    l1.reverse()
    l1.displaylList()
    l1.addIdx(2,9)
    l1.displaylList()
    l1.remove(9)
    l1.displaylList()
    l1.removeIdx(2)
    l1.displaylList()

test()
