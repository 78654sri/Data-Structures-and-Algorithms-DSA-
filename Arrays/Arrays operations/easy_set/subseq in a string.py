def is_subsequence(subseq, full_string):
    subseq_index = 0
    full_string_index = 0

    while subseq_index < len(subseq) and full_string_index < len(full_string):
        if subseq[subseq_index] == full_string[full_string_index]:
            subseq_index += 1
        full_string_index += 1

    return subseq_index == len(subseq)

# Example usage
subseq = "abc"
full_string = "aebdc"
result = is_subsequence(subseq, full_string)
print(f'Is "{subseq}" a subsequence of "{full_string}"? {result}')
"""=========================================================================================="""
subseq = "abc"
full_string = "aebdc"
sub_seq=0
for i in range(len(full_string)):
    if full_string[i]==full_string[sub_seq]:
        sub_seq+=1
        if sub_seq==len(sub_seq):
            break
if sub_seq==len(sub_seq):
    print("yes")
else:
    print("no")
