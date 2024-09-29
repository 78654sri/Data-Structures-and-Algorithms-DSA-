def intersection_two_sorted_arrays(a, b):
    ans = []
    temp = [0] * len(b)
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j] and temp[j] == 0:
                ans.append(a[i])
                temp[j] = 1
                break
            elif a[i] < b[j]:
                break
    
    return ans
a=[2 ,3 ,3 ,3 ,4]
b=[3 ,3 ,4,4]
result=intersection_two_sorted_arrays(a, b):
print(result)


def intersection2sortedarrays(a, b):
    ans = []
    i, j = 0, 0
    m, n = len(a), len(b)
    while i < m and j < n:
        if a[i] == b[j]:
            ans.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return ans
a=[2 ,3 ,3 ,3 ,4]
b=[3 ,3 ,4,4]
result=intersection_two_sorted_arrays(a, b):
print(result)
