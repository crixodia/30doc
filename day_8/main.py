class LinkedList(object):
    # ListNode won't be used out of LinkedList, so it is better to create an Inner Class
    class ListNode(object):

        def __init__(self, val, _next=None):
            self.val = val
            self.next = _next

    def __init__(self, val, next=None):
        self.node = self.ListNode(val, next)

    def __str__(self):
        s = ""
        current = self.node
        while current:
            s += f"[{current.val}]->"
            current = current.next
        s += "[None]"
        return s

    def push(self, val):
        if not self.node:
            self.node = self.ListNode(val)

        current = self.node
        while current.next:
            current = current.next
        current.next = self.ListNode(val)

    def pop(self) -> object:
        if not self.node:
            return None

        if not self.node.next:
            r = self.node.val
            self.node = None
            return r

        current = self.node
        last = current
        while current.next:
            last = current
            current = current.next

        last.next = None
        return current.val

    def shift(self) -> object:
        if not self.node:
            return None

        r = self.node.val
        self.node = self.node.next
        return r

    def unshift(self, val) -> object:
        if not self.node:
            self.node = self.ListNode(val)

        self.node = self.ListNode(val, self.node)


if __name__ == "__main__":
    L = LinkedList(1)
    print(f"init:\t1\t{L}")

    L.push(2)
    print(f"push:\t2\t{L}")

    L.push(3)
    print(f"push:\t3\t{L}")

    L.unshift(0)
    print(f"unshift:0\t{L}")

    L.unshift(-1)
    print(f"unshift:-1\t{L}")

    print(f"pop:\t{L.pop()} \t{L}")
    print(f"shift:\t{L.shift()} \t{L}")
    print(f"pop:\t{L.pop()} \t{L}")
    print(f"shift:\t{L.shift()} \t{L}")
    print(f"shift:\t{L.shift()} \t{L}")
