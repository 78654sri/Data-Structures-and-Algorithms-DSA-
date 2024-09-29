def find_pairs_with_product(arr, target_product):
    pairs = []
    seen = set()

    for num in arr:
        if num == 0 and target_product == 0:
            continue
        if num != 0 and target_product % num == 0:
            complement = target_product // num
            if complement in seen:
                pairs.append((complement, num))
        seen.add(num)

    return pairs

# Example usage:
arr = [2, 4, 1, 6, 5, 10, -1]
target_product = 20
print(find_pairs_with_product(arr, target_product))  # Output: [(4, 5), (2, 10)]
