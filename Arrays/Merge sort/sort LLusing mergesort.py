class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def find_mid(start, end):
    slow = fast = start
    while fast != end and fast.next != end:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge(left, right):
    dummy = ListNode(0)
    tail = dummy
    while left and right:
        if left.val < right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    tail.next = left or right
    while tail.next:
        tail = tail.next
    
    return dummy.next

def merge_sort(head, end):
    if head == end or head is None or head.next == end:
        return head
    
    mid = find_mid(head, end)
    left = merge_sort(head, mid)
    right = merge_sort(mid, end)
    
    return merge(left, right)

# Helper function to print the linked list
def print_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Example usage
head = ListNode(4)
head.next = ListNode(2)
head.next.next = ListNode(1)
head.next.next.next = ListNode(3)

print("Original list:")
print_list(head)

sorted_head = merge_sort(head, None)

print("Sorted list:")
print_list(sorted_head)
