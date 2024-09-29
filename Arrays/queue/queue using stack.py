class QueueStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def enqueue(self, val):
        self.stack1.append(val)
    def dequeue(self):
        if not self.stack2 and not self.stack1:
            return None
        elif not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()
        else:
            return self.stack2.pop()

q = QueueStack()
q.enqueue(2)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
q.enqueue(3)
q.enqueue(3)
q.dequeue()
print(q.stack1)