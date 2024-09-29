def countDistinct(arr, n, k):
    res = []

    for i in range(n - k + 1):
        dist_count = 0
        s = set()
        for j in range(i, i + k):
            s.add(arr[j])

        dist_count = len(s)
        res.append(dist_count)

    return res

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
n = len(arr)
k = 3
print(countDistinct(arr, n, k)) 