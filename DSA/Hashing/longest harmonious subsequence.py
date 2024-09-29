arr=[1,2,3,4,5]
arr=[4,3,2,5]

map={}
result=0
for ele in arr:
    map[ele]+=1
for key in map:
    if key+1 in map.keys():
        result=max(result,map[key]+map[key+1])
    if key-1 in map.keys():
        result=max(result,map[key]+map[key-1])
print(result)

    


