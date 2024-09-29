#Brute force


def count_frequencies(arr):
    freq_dict = {}
    for i in range(len(arr)):
        k = arr[i] - 1  # because output array is 1-indexed
        if k in freq_dict:
            continue
        freq_dict[k] = 1
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                freq_dict[k] += 1
    for key, value in freq_dict.items():
        print(value)


arr = [1, 1, 1, 1, 2, 3, 3, 3, 3, 3, 3, 4, 5]
count_frequencies(arr)


#optimal Approach

def frequencyCount(arr, N):
    map = {}
    for i in range(N):
        if arr[i] in map:
            map[arr[i]] += 1
        else:
            map[arr[i]] = 1
            
    for j in range(1, N):
        if j in map:
            arr[j-1] = map[j]
        else:
            arr[j-1] = 0

# Example usage:
arr = [1, 2, 2, 3, 3, 3]
N = len(arr)
frequencyCount(arr, N)
print(arr)  