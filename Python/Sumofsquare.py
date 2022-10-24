def sumoddsquares(k):
    x=0
    range_ = list(range(1,k))
    for i in range_:

        if i % 2==0:
            f=0
        else:
            x += i*i
    
    return x
        
sumoddsquares(5)
