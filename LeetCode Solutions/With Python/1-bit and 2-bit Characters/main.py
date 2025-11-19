#bits = [1,0,0] # return True

#bits = [1,1,1,0] # return False

#bits = [1,1,1,1] # return False 

bits = [1,1,0,0,0,1,0] # return False 

#bits = [1,1,0,1] # return False

def isOneBitCharacter(bits: list) -> bool:

    i = 0 
    n = len(bits)
    
    while i < n - 1:
        
        if bits[i] == 1:
            i += 2
        else:
            i += 1
            
    return i == n - 1

print(isOneBitCharacter(bits))