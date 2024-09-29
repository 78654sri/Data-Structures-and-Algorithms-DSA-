#creating an empty array
import array as arr

array1=arr.array('i')
print(array1)


#time complexity:O(1)
#space complexity:O(1)


#creating an array with elements
#Declaring array using the list in Python.
arr=[1,4,3,55,6,11]
for i in range(0,len(arr)):
    print(arr[i])

#Declaring array using the array module in Python

import array as arr

array1=arr.array('i',[1,3,2,4,5])
for i in range(0,len(array1)):
    print(array1[i])


#time complexity:O(N)
#space complexity:O(N)