#Removing from the beginning of the array
arr=[1,3,4]
length = len(arr)
for i in range(0,length-1):#------------ O(N)
    arr[i] = arr[i+1]
arr.pop()#--------------------- O(1)

print(arr)

#or
arr=[1,3,4]
if arr:
    arr.pop(0)
print(arr)

#Removing from the end of the array

arr=[2,4,5]
if arr:
    arr.pop()
print(arr)

 #Remove value at index i

def remove(array, i, length):
    for index in range(i + 1, length):#------------ O(N)
        array[index - 1] = array[index]
    array.pop()

arr = [1, 3, 4, 5, 6]
length = len(arr)
remove(arr, 2, length)  

print(arr) 
#===================================================================================================================

#TOTALLY

# time complexity:O(N)
# space complexity:O(1)