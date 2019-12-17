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


    def addIdx(self, v, i):
        n = self.snode
        j = 0
        prev = None
        curr = None
        next = None
        while n is not None:
            # Add to the head
            curr = n
            next = curr.next
            if i == 0:
                self.snode = node(v)
                self.snode.next = n
                break
            elif i == j:
                temp = node(v)
                prev.next = temp
                temp.next = curr
                break
            j += 1
            prev = curr
            n = n.next



    def displaylList(self):
        if self.snode is None:
            pass
        else:
            n  = self.snode
            while n is not None:
                print(str(n.value), end=' ')
                n = n.next
            print()


    def removeVal(self, val):
        if self.snode is None:
            pass
        else:
            n = self.snode
            curr = None
            prev = None
            next = None
            while n is not None:
                curr = n
                next = curr.next
                if curr.value == val:
                    # If its a root node
                    if prev is None:
                        self.snode = n.next
                        break
                    # if curr is last node
                    elif next is None:
                        prev.next = None
                        break
                    # If any other middle node
                    elif prev is not None and next is not None:
                        prev.next = next
                        break
                else:
                    prev = curr
                    n = n.next


    def reverse(self):
        n = self.snode
        prev = None
        curr = None
        next = None
        while n is not None:
            curr = n
            n = curr.next
            curr.next = prev
            prev = curr
            if n is not None:
                self.snode = n

def test_simple_linkedlist():
    l1 = linkedlist(node(9))
    l1.add(1)
    l1.add(2)
    l1.add(3)
    l1.add(4)
    l1.displaylList()
    l1.reverse()
    l1.displaylList()

test_simple_linkedlist()