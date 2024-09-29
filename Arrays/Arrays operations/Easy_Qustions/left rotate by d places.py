def leftRotate(l,d):
    for i in range(0,d):
        l.append(l.pop(0))

l=[10,20,30,40,50]
d=3
leftRotate(l,d)
print(l)



def rightRotate(l, d):
    for i in range(0, d):
        l.insert(0, l.pop())


l = [10, 20, 30, 40, 50]
d = 3
rightRotate(l, d)
print(l) 



def left_rotate_using_stacks(arr, d):
    n = len(arr)
    if n == 0 or d == 0:
        return arr
    
  
    d = d % n
    
    stack1 = []
    stack2 = []
    
  
    for i in range(d):
        stack1.append(arr[i])
    
    
    for i in range(d, n):
        stack2.append(arr[i])
    
    
    result = []
    

    while stack2:
        result.append(stack2.pop(0))
    
   
    while stack1:
        result.append(stack1.pop(0))
    
    return result

arr = [1, 2, 3, 4, 5, 6]
d = 2
result = left_rotate_using_stacks(arr, d)
print(result) 


def reverse(l,b,e):
    while b<e:
        l[b],l[e]=l[e],l[b]
        b=b+1
        e=e-1


def leftRotate(l,d):
    n=len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)


l=[10,20,30,40,50]
d=3
leftRotate(l, d)
print(l)
