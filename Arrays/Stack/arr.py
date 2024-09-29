def SumOfkConsicutive(arr,k):#arr=[8,9,10,11] 17,19,21
   list=[]          
                    
   for i in range(len(arr)+1): #i=0,1,2
      sum=0    
      for j in range(i,k):#j=0,2+0   3,4,5
          sum+=arr[j] 
      list.append(sum)  
   return list
arr=[8,9,10,11]
k=3
ans=SumOfkConsicutive(arr,k)
print(ans)