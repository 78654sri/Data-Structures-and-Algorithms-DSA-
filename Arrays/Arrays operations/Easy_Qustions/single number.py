def findunique(arr):
    size = len(arr)
    for i in range(size):
        for j in range(size):
            if i != j:
                if arr[i] == arr[j]:
                    break
        if j == size - 1:
            return arr[i]
    return float('-inf')

# Example usage
arr = [2, 3, 5, 4, 5, 3, 4]
print(findunique(arr))  # Output: 2

"""==============================================================================="""
def findunique(input):
    count_dict = {}
    for num in input:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    for num, count in count_dict.items():
        if count == 1:
            return num

arr = [2, 3, 5, 4, 5, 3, 4]
print(findunique(arr))  # Output: 2








def findunique(input):
    input.sort()
    for i in range(0, len(input) - 1, 2):
        if input[i] != input[i + 1]:
            return input[i]
    return input[-1]


arr = [2, 3, 5, 4, 5, 3, 4]
print(findunique(arr)) 

"""==============================================================================="""
def findunique(input):
    xor=0
    for num in input:
        xor=xor^num
    return xor


arr = [1,2,1,3,2]
print(findunique(arr)) 

































"""==============================================================================="""

def findunique(input):
    unique_elements = set()
    for num in input:
        if num in unique_elements:
            unique_elements.remove(num)
        else:
            unique_elements.add(num)
    return unique_elements.pop()


arr = [2, 3, 5, 4, 5, 3, 4]
print(findunique(arr))  

"""==============================================================================="""
def findunique(input):
    answer = 0
    for num in input:
        answer ^= num
    return answer
