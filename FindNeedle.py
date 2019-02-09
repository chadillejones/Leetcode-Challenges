def findNeedle(needle, stack):
    if needle =="":
        print(0)
        return 0
        
        
    x=0
    count=0
    for i in range(0,len(stack)):
        if needle[x]==stack[i]:
            y=i+1
            for w in range(1,len(needle)):
                if needle[w]==stack[y]:
                    count+=1
                else:
                    break
            if count==len(needle)-1:
                print(i)
                return i
    print(-1)
    return(-1)
    
findNeedle("aa","aabbaa")