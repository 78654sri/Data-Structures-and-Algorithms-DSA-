def get_union(a, b):
    ans = []
    s = set(a + b)
    ans.extend(s)
    return ans


def get_union(a, b):
    i, j = 0, 0
    ans = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            if not ans or a[i] != ans[-1]:
                ans.append(a[i])
            i += 1
        else:
            if not ans or b[j] != ans[-1]:
                ans.append(b[j])
            j += 1
    while j < len(b):
        if not ans or b[j] != ans[-1]:
            ans.append(b[j])
        j += 1
    while i < len(a):
        if not ans or a[i] != ans[-1]:
            ans.append(a[i])
        i += 1
    return ans