def Palindrome(stringA):
    oddcount=0
    stringA=stringA.replace(" ","")
    stringA=stringA.replace(",","")
    stringA=stringA.lower()
    
    for i in range(0,len(stringA)):
        pholder=stringA[i]
        x=stringA.count(pholder)
        
        if x % 2 !=0:
            oddcount+=1
            
    
    if oddcount>1:
        print(False)
        
        return False
    else:
        print(True)
        return True

Palindrome("tattarrattta")