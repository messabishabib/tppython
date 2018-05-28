def puissance(n,k):    
    r=1
    if k==1:
        return n
        
    if k%2==0:
        
        r=puissance(n,k/2)
        return r*r
    else:
    
        r=puissance(n,(k-1)/2)
        return r*r*n
    
puissance(3,4)
