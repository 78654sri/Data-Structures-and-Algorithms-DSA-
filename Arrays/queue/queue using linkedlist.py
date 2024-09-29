class _Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class QueuesLinked:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size

    def isempty(self):
        return self.size == 0

    def enqueue(self, val):
        newest = _Node(val)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            self.tail = newest
        self.size += 1

    def dequeue(self):
        if self.isempty():
            print('Queue is empty')
            return
        e = self.head.val
        self.head = self.head.next
        self.size -= 1
        if self.isempty():
            self.tail = None
        return e

    def first(self):
        if self.isempty():
            print('Queue is empty')
            return
        return self.head.val

    def display(self):
        p = self.head
        while p:
            print(p.val, end=' <-- ')
            p = p.next
        print()

Q = QueuesLinked()
Q.enqueue(5)
Q.enqueue(3)
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
ele = Q.dequeue()
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
print('Removed Element:', ele)
print('Is Queue Empty:', Q.isempty())
Q.enqueue(7)
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
Q.enqueue(12)
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
ele = Q.dequeue()
print('Queue:')
Q.display()
print('Queue Length:', len(Q))
print('Removed Element:', ele)
print('First Element:', Q.first())