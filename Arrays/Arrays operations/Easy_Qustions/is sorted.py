def is_sorted(a, n):
    for i in range(n - 1):
        if a[i] > a[i + 1]:
            return False
    return True
a=[1,2,3,4,5]
n=len(a)
result=is_sorted(a, n)
print(result)