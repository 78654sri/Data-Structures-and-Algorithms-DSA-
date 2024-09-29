def canArrange(arr, k):
    map = {}
    n = len(arr)

    for i in range(n):
        current_value = arr[i]
        current_remainder = ((current_value % k) + k) % k  # Ensure positive remainder for negative values
        map[current_remainder] = map.get(current_remainder, 0) + 1

    for key in map:
        if key == 0:
            if map[key] % 2 != 0:
                return False
        elif k - key in map:
            if map[key] != map[k - key]:
                return False
        else:
            return False

    return True


arr = [1, 2, 3, 4, 5, 10, 6, 7, 8, 9]
k = 5
print(canArrange(arr, k))  
