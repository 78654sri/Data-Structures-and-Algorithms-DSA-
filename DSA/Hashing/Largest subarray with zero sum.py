def maxLen(A, n):
    maxlen = 0

    for i in range(n):
        for j in range(i, n):
            sum = 0
            for k in range(i, j+1):
                sum += A[k]

            if sum == 0:
                maxlen = max(maxlen, j - i + 1)

    return maxlen
arr = [5, 8, 9, -10,10, -10,10, 6, 7, 8]
n = len(arr)
print(maxLen(arr, n)) 



def maxLen(arr, n):
    max_len = 0

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]
            if curr_sum == 0:
                max_len = max(max_len, j - i + 1)

    return max_len
arr = [5, 8, 10, -10, 10, -10,6, 7, 8]
n = len(arr)
print(maxLen(arr, n)) 

def maxLen(a, n):
    sum_val = 0
    ans = 0
    m = {}
    m[0] = -1
    
    for i in range(n):
        sum_val += a[i]
        if sum_val in m:
            ans = max(ans, i - m[sum_val])
        else:
            m[sum_val] = i
    
    return ans

# Example usage:
arr = [5, 8, 10, -10,10, -10, 6, 7, 8]
n = len(arr)
print(maxLen(arr, n)) 