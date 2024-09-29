arr=[1,3,2,4]
index=3
for i in range(0,len(arr)-1):#------------------------------>> O(1)
    if i==index:
        break
print(arr[i])

# time complexity : O(N)
# space complexity : O(1)