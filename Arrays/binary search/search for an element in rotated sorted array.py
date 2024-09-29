def find_starting_index(arr):
    left, right = 0, len(arr) - 1
    
    if arr[left] < arr[right]:
        return 0
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > arr[mid + 1]:
            return mid + 1
    
        if arr[mid] >= arr[left]:
            left = mid + 1
        else:
            right = mid - 1
    
    return 0




def search_rotated_array(arr, target):
    n = len(arr)
    rotation_index = find_starting_index(arr)
    
    left, right = 0, n - 1
    
    while left <= right:
        mid = (left + right) // 2
        real_mid = (mid + rotation_index) % n
        
        if arr[real_mid] == target:
            return real_mid
        elif arr[real_mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1
arr = [4, 5, 6, 7, 0, 1, 2]
target = 0
index = search_rotated_array(arr, target)
print(index )