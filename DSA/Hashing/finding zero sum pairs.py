def pairSum(arr):
    # Create a dictionary to store the frequency of each element
    frequencyMap = {}
    
    # Iterate through each element in the array
    for element in arr:
        complement = -element  # Find the complement that would sum to zero
        
        # Check if the complement exists in the frequency map
        if complement in frequencyMap:
            # Print the pair as many times as complement appears
            for _ in range(frequencyMap[complement]):
                print(f"Pair found: ({complement}, {element})")
        
        # Update the frequency of the current element in the map
        if element in frequencyMap:
            frequencyMap[element] += 1
        else:
            frequencyMap[element] = 1

# Example usage
arr = [2, -2, 3, -3, 4, -4, -2, 2]
pairSum(arr)
