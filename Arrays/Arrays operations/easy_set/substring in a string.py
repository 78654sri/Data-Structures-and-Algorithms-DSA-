def is_substring(substring, full_string):
    len_sub = len(substring)
    len_full = len(full_string)

    # Loop through the full string
    for i in range(len_full - len_sub + 1):
        # Check if the substring matches the current slice of the full string
        if full_string[i:i + len_sub] == substring:
            return True
    return False

# Example usage
substring = "abc"
full_string = "aebdcabc"
result = is_substring(substring, full_string)
print(f'Is "{substring}" a substring of "{full_string}"? {result}')
"""==================================================================================="""
def is_substring(substring, full_string):
    len_sub = len(substring)
    len_full = len(full_string)
    i = 0
    while i <=len_full - len_sub + 1:
        
        j = 0
        while j < len_sub :
            if full_string[i] == substring[j]:
                 j += 1
                 i += 1
            else:
                j=0
                i += 1
        if j == len_sub:
            return True
    return False

# Example usage
substring = "abc"
full_string = "aebdcabc"
result = is_substring(substring, full_string)
print(f'Is "{substring}" a substring of "{full_string}"? {result}')


