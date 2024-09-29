def longest_substring_without_repeating(s):
    h = {}  # Dictionary to store the last index of each character
    start = 0  # Start index of the current substring
    length = 0  # Length of the longest substring found

    for i, char in enumerate(s):
        if char in h:
            start = max(start, h[char] + 1)
        h[char] = i
        length = max(length, i - start + 1)

    return length

# Test the function
s = "abcabcbbderg"
print(longest_substring_without_repeating(s))