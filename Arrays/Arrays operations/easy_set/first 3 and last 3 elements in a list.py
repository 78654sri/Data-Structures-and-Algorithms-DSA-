list_ = ["he","ff","ll","fg","kk","ft","fr","ww"]
N = len(list_)

arr = [0] * 6
n = len(arr)
for i in range(3):
    arr[i] = list_[i]
    arr[n-i-1] = list_[N-i-1]  # Corrected index calculation

print(arr)
