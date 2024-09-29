class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class StackLinked:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def push(self, val):
        new_node = Node(val)
        if self.is_empty():
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            element = self.head.val
            self.head = self.head.next
            self.size -= 1
            return element

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        else:
            return self.head.val
        
    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end="->")
            temp = temp.next
        print()

s = StackLinked()
s.push(10)
s.push(20)
s.push(8)
s.display()