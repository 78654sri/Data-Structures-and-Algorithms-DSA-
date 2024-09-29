def find_symmetric_pairs(arr):
    m = {}
    ans = []

    # First pass: store each pair in the map
    for pair in arr:
        m[pair[0]] = pair[1]

    # Second pass: find symmetric pairs
    for pair in arr:
        if pair[1] in m and m[pair[1]] == pair[0]:
            ans.append((pair[0], pair[1]))
            m.pop(pair[1])

    return ans
