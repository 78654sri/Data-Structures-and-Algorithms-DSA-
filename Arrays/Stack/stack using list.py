class Stack:
    def __init__(self):
        self.stack = []

    def __len__(self):
        return len(self.stack)
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, e):
        self.stack.append(e)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.stack[-1]

s = Stack()
s.push(1)
s.push(5)
s.push(4)
print(s.stack)
print(len(s))
print(s.peek())
print(s.pop())
print(s.stack)