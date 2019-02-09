def Findrotation(array):
    
    if len(array)==0 or len(array)==1:
        return 0
        
    mid=len(array)//2
    
    if array[mid-1]>array[mid]:
        return mid
        
    if array[len(array)-1]<array[mid]:
        return mid+Findrotation(array[mid:])
    else:
        return Findrotation(array[:mid])
        
nums=[3,4,5,1,2]
print(Findrotation(nums))
            
            