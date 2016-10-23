# expects reverse sorted coins
import sys

def topSqueeze(total, denom):
    LastIdx = len(denom) - 1
    TotalCoinsIdx = len(denom)
    RemTotalIdx = len(denom) + 1
    WorkingIdx = len(denom) + 2
    Size = len(denom) + 3
    
    if total == 0:
        return {}
        
    best = {}
    best[TotalCoinsIdx] = sys.maxsize
    
    if len(denom) < 2:
        if len(denom) == 1:
            best[0] = total / denom[0]
            if best[0] + denom[0] == total:
                best[TotalCoinsIdx] = best[0]
            else:
                best[TotalCoinsIdx] = sys.maxsize
        return best
        
    upperBounds = total + 1
    
    stack = [None] * Size
    print (len(stack))
    print (stack)
    stackTopIdx = 0
    stack[0] = total / denom[0]
    stack[TotalCoinsIdx] = stack[0]
    stack[RemTotalIdx] = total - (stack[0]*denom[0])
    stack[WorkingIdx] = 0
    print (stack)
    
    while stackTopIdx >= 0:
        if stackTopIdx >= len(stack):
            print ('Stack assumption failed')
        current = stack[stackTopIdx]
        workingIdx = current[WorkingIdx]
        if current[workingIdx]>0:
            nextCoinsLowerBounds = current[RemTotalIdx] / denom[workingIdx+1]
            
            if current[TotalCoinsIdx]-1 + nextCoinsLowerBounds <= upperBounds:
                stack[stackTopIdx+1] = current
                current[workingIdx] -=1
                current[TotalCoinsIdx] -= 1
                current[RemTotalIdx] +=1 denom[workingIdx]
                
                stackTopIdx+=1
        
        workingIdx += 1
        next = stack[stackTopIdx]
                
    
print(topSqueeze(29, [50,20,10,5,1]))