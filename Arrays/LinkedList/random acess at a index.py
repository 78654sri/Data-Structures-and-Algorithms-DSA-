def search(self, key):

    temp = self.head
    i = 0
    while temp:
        if temp.data == key:
             return i
        temp = temp.next
        i += 1

    return -1
# Operation	                Time Complexity		Space Complexity

# Insertion at Beginning        O(1)	           O(1)
# Insertion at End	            O(n)	           O(1)
# Insertion at Given Position	O(n)		       O(1)
# Deletion at Beginning	        O(1)	     	   O(1)
# Deletion at End              	O(n)	     	   O(1)
# Deletion at Given Position	O(n)	           O(1)
# Searching	                    O(n)	     	   O(1)
# Accessing by Index           	O(n)		       O(1)
