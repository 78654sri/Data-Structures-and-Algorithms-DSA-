#insert element at beginning of the array
arr = [1, 2, 3]
x = 2
arr.append(0)  
for i in range(len(arr)-2, -1, -1):#--------------- >O(N)
    arr[i+1] = arr[i]
arr[0] = x #-------------------- O(1)
print(arr)


#insert element at given index 
arr=[1,4,3,2]
index=2
ele=7
arr.append(0)
for i in range(len(arr)-2, index-1, -1):#----------------O(N)
    arr[i+1] = arr[i]
arr[index]=ele#----------------O(1)
print(arr)
    

    
#insert element at end of the array
arr=[1,2,34]
ele=5
arr.append(ele)
print(arr)

#=========================================================

#TOTALLY

# time complexity:O(N)
# space complexity:O(1)