class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.len = 0
    
    def addHead(self, data):
        node = Node(data)
        if self.len == 0:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        self.len += 1
    
    def addEnd(self, data):
        if self.len == 0:
            self.addHead(data)
        else:
            node = Node(data)
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = node
            self.len += 1
    
    def addAtIndex(self, data, index):
        if index < 0:
            raise IndexError('Provide a positive value')
        if index == 0:
            self.addHead(data)
        elif index >= self.len:
            self.addEnd(data)
        else:
            node = Node(data)
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            node.next = temp.next
            temp.next = node
            self.len += 1
    
    def removeHead(self):
        if self.len == 0:
            raise ValueError("Linked list is empty")
        else:
            self.head = self.head.next
            self.len -= 1

    def removeEnd(self):
        if self.len == 0:
            raise ValueError("Linked list is empty")
        else:
            temp = self.head
            while temp.next.next is not None:
                temp = temp.next
            temp.next = None
            self.len -= 1
    
    def removeAt(self, index):
        if index < 0 or index >= self.len:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.removeHead()
        else:
            temp = self.head
            for i in range(index - 1):
                temp = temp.next
            temp.next = temp.next.next
            self.len -= 1

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

# Example usage
ll = LinkedList()
ll.addEnd(1)
ll.addEnd(2)
ll.addEnd(3)
ll.addAtIndex(0, 0)
ll.addAtIndex(1.5, 2)
ll.removeAt(3)
ll.display()  # Output should be: 0 -> 1 -> 1.5 -> 3 -> None
