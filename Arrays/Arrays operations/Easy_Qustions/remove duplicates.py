def remove_duplicates(a, n):
    s = set()
    for i in range(n):
        s.add(a[i])
    j = 0
    for k in s:
        a[j] = k
        j += 1
    return len(s)
a=[1,1,2,3,3,4]
n=len(a)
result=remove_duplicates(a, n)
print(result)


def remove_duplicates(a, n):
    rest=1
    for i in range(1,n):
        if a[rest-1]!=a[i]:
            a[rest]=a[i]
            rest+=1
    return a[:rest]

a=[1,2,2,3,3,3]
n=len(a)
result=remove_duplicates(a, n)
print(result)


def remove_duplicates(a, n):
    i=1
    j=2
    while j<=n-1:
        if a[i]==a[j]:
            j+=1
        else:
            a[i+1]=a[j]
            i+=1
    return a[:i+1]
a=[1,2,2,3,4,4,5,6]
n=len(a)
result=remove_duplicates(a, n)
print(result)