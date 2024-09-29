def circle_passing(n):
    start = 0
    count = 1  # Starting from index 0, so initialize count to 1
    num = (start + 2) % n  # First step from start
    
    while num != start:
        num = (num + 2) % n   
        count += 1
    
    return count == n
result = circle_passing(6)
print(result)  # Output should be True if it visits all elements

list1 = [1, 2, 3]
list2 = list1 * 2

print(list2)  # Output: [1, 2, 3, 1, 2, 3]

